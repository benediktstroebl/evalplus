from typing import List, Any
def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [val for val in values if isinstance(val, int)]
    return result