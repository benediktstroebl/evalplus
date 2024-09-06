from typing import List, Optional
def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter a list of Python values to a list of integers.

    Args:
        values (List[Any]): A list of any Python values.

    Returns:
        List[int]: A list containing only integers from the input list.

    Example:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [val for val in values if isinstance(val, int)]