from typing import List
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else [x + delimeter for x in numbers[1:] + [numbers[0] + delimeter]]