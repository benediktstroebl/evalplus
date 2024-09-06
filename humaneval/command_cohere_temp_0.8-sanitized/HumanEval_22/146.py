from typing import List, Optional
def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    res: List[int] = []
    for value in values:
        if isinstance(value, int):
            res.append(value)
    return res