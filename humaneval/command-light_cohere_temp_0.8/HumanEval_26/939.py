```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen and num not in numbers[numbers.iset]]
    told in the input and it can be used for testing. 
numbers = [1, 2, 3, 2, 4]
result_test = remove_duplicates(numbers)
print("Test 1:", result_test)
numbers_set = set(numbers)
print("Test 2:", list(numbers_set))
print("Test 3:", result_test == numbers)
```