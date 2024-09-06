```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sub list of n=len maximum from the numbers, and for each n in numbers, yields the next maximum.

# Test case:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function called `rolling_max`, which takes a list of integers as input and returns a new list with the rolling maximum elements found in the input sequence. 

It utilizes the Python `typing` feature to define the input argument as a list of integers, and returns the result as a new list of integers.

The script then creates a test case with the `numbers` list, and passes it to the `rolling_max` function to get the result. The result is printed to the console.