from typing import List, Any
def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    Args:
        values (List[Any]): Mixed list of values

    Returns:
        List[int]: Filtered list of integers
    """
    return [x for x in values if isinstance(x, int)]