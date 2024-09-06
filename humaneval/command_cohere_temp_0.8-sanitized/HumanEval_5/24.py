from typing import List
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimiter + numbers + [delimiter]