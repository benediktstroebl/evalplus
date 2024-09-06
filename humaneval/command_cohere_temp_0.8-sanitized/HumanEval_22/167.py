from typing import List
def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = [val for val in values if isinstance(val, int)]
    return integers