```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, i in zip(numbers, numbers) if i < numbers[i]]

# Test case:
numbers = [1, 2, 3, 4, 3, 2, 1]
result = rolling_max(numbers)
print(result)
``` 
This solves the given problem: 
- Takes a list of integers.
- Using a list of numbers as the sequence, it generates a new list containing the maximum element from the sequence at each moment. 
This function achieves this by using a list comprehension with a generator expression and the zip function.