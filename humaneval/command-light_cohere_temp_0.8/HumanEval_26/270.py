```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]
This function utilizes the built-in `count()` method along with list comprehension to achieve the desired result. It removes duplicates from the big collection of integers.