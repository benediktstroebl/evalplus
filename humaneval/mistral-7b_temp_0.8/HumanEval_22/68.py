from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # filter() accepts a function that takes a single value as an argument
    # and returns True or False depending on whether or not the value is
    # to be included in the resulting list.
    return list(filter(lambda value: isinstance(value, int), values))

