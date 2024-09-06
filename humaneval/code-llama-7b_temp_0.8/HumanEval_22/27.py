from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    result: List[int] = []
    for value in values:
        try:
            value_as_int = int(value)
            result.append(value_as_int)
        except ValueError:
            pass
    return result

