from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]
numbers = [1, 2, 3, 2, 4]