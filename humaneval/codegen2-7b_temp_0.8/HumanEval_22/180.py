from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    filtered_values = []
    for value in values:
        if isinstance(value, (int, float)):
            filtered_values.append(int(value))
        else:
            filtered_values.append(value)
    return filtered_values

