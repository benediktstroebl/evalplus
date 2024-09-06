from typing import List, Optional
def filter_integers(values: List[Any]) -> List[int]:
    result: List[int] = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result