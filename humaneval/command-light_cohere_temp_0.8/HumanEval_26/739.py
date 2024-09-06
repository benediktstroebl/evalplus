```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.keys()]]
keys() is a helper function that returns a set of distinct elements from the numbers list using the keys method.

# You can add more extensive tests on the function to verify its correctness.