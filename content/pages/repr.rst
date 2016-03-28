What's the difference between str() and repr()?
===============================================

When it comes to :code:`__str__` and :code:`__repr__`,
they often seem to be confusing.
What is the difference? How do we implement them correctly?

There are three main points:

* The default implementation is useless (it's hard to think of one which wouldn't be, but yeah)
* :code:`__repr__` goal is to be unambiguous
* :code:`__str__` goal is to be readable
* Containers' :code:`__str__` uses contained objects' :code:`__repr__`

Default implementation is useless
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is mostly a surprise because Python’s defaults tend to be fairly useful.
However, in this case, having a default for :code:`__repr__` which would act like:

.. code::

    return "%s(%r)" % (self.__class__, self.__dict__)

would have been too dangerous
(for example, too easy to get into infinite recursion if objects reference each other).
In the face of temptation, Python refuses to guess.
Note that there is one default which is useful:
if :code:`__repr__` is defined, and :code:`__str__` is not,
the object will behave as though :code:`__str__==__repr__`.

This means, in simple terms:
almost every object should have a functional :code:`__repr__`
that's usable for understanding the object.
Implementing :code:`__str__` is optional:
it is useful for "pretty print" functionality
(for example, used by a report generator).

The goal of __repr__ is to be unambiguous
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Logging is the lifeblood of any decent fire-and-forget server system.
Python makes it easy to log: with maybe some project specific wrappers, a simple:

.. code::

    log(INFO, "I am in the weird function and a is", a,
              "and b is", b,
              "but I got a null C — using default", default_c)

For this to work, every object must have a useful repr.
This is why the "eval" thing comes up:
if there is enough information so :code:`eval(repr(c))==c`,
that means :code:`__repr__` contains everything there is to know about c.
If that's easy enough, at least in a fuzzy way, than it is a good option.
If not, it needs to have enough information about c anyway.

It is often useful to use an eval-like format:
:code:`"MyClass(this=%r,that=%r)" % (self.this,self.that)`.
It does not mean that it is actually possible to construct :code:`MyClass`,
or that those are the right constructor arguments -- but it is a useful form to express
"this is everything there is to know about this instance".

Note the :code:`%r` above, not :code:`%s`.
Always use :code:`repr()` or,
equivalently, the :code:`%r` formatting character,
inside :code:`__repr__` implementation.
Otherwise the goal of repr is defeated --
it would not be possible to differentiate between :code:`MyClass(3)` and :code:`MyClass("3")`.

The goal of __str__ is to be readable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Specifically, it is not intended to be unambiguous -- for example, :code:`str(3)==str("3")`.
ikewise, when implementing an IP abstraction, having the str of it look like :code:`192.168.1.1` is just fine.
When implementing a date/time abstraction,
the str can be :code:`2010/4/12 15:35:22`.
The goal is to represent it in a way that a user, not a programmer,
would want to read it.
Chop off useless digits, pretend to be some other class --
as long is it supports readability, it is an improvement.

Containers' str() calls contained objects' repr()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is a little surprising, but how readable would this be?

.. code::

    [my name is, 3, hello
    world, this is a list, oh I don't know, containing just 4 elements]

The strings in a container would find it way too easy to disturb its string representation.
In the face of ambiguity, remember, Python resists the temptation to guess.

Summary
^^^^^^^

Implement :code:`__repr__` for each class you implement.
This should be second nature.
Implement :code:`__str__` if it would be useful to have a string version
which errs on the side of more readability
in favor of more ambiguity.
