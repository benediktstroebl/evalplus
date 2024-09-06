from typing import List, Optional
def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter a list of values down to only integers.

    Args:
        values (List[Any]): The list of values to filter.

    Returns:
        List[int]: A new list containing only the integers from the input list.

    Example:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]