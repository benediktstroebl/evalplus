```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:]) for i in range(len(numbers))]]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Expected output: [1, 2, 3, 3, 3, 3, 4, 4]
```
This Python code defines a function called "rolling_max" that takes a list of integers as input and generates a new list containing the maximum value from the list's elements, calculated using a rolling window approach. The code then demonstrates the demonstration of the function's output by creating a sample list of integers and passing it as an argument to the "rolling_max" function. The expected output of this list of integers matches the desired result of the rolling_max function.