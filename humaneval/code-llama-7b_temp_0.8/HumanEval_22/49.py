from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # so far we only know that values are iterable
    # and contain at least one element
    filtered_values = [value for value in values if isinstance(value, int)]

    # one additional check would be needed here to check
    # if items in `filtered_values` are actually integers

    return filtered_values

