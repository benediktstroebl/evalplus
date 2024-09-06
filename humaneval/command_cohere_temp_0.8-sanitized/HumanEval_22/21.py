from typing import List
def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = [item for item in values if isinstance(item, int)]
    return integers