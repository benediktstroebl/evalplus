from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [int(x) for x in values if x is not None and x is not a string and x is not a list and x is not a tuple and x is not a dict and x is not an empty dictionary and x is not NoneType()]