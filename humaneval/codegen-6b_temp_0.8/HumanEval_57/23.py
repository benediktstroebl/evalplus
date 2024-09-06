

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))



"""
-----------------------------------------------------------------------
If for some reason you have a list of non-nondominating things that you
want to use for a plot, and you want them to plot in order, you can do
so by using the sorted() function.

The sorted() function returns a new list, but does not change the original
list. It is a method of the list class.

sorted() takes a single argument: some iterable object.

This function does not work with strings. It works with tuples, but not with
lists, sets, or dictionaries.

The first argument to sorted() is the list of things you want to sort.

You can specify key functions by passing a second argument to the
function. The key function defines what the index of an element is, for
example, in a list of 2-tuples. You can use any function that takes one
argument (whatever is at that index in the tuple), and it will be used to
determine the value of the index.

"""