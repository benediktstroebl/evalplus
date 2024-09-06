from typing import List, Optional
def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter a list of Python values and return a list of integers.

    Args:
        values (List[Any]): The input list of values, which could be of any type.

    Returns:
        List[int]: A list containing only the integers from the input list.

    Example:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    result: List[int] = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result