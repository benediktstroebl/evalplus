from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # Method 1
    # return [int(x) if isinstance(x, int) else x for x in values]
    # Method 2
    return [x[1] for x in enumerate(values) if isinstance(x[1], int)]

