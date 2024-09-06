from typing import List, Any
def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [num for num in values if isinstance(num, int)]