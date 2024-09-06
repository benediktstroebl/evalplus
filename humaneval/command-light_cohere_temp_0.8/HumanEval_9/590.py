```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort(reverse=True)
    m = numbers[0]
    for n in numbers[1:]:
        m = max(n, m)
    return [m]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)

numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
print(result)

numbers = [1, 2, 3, 4, 6]
result = rolling_max(numbers)
print(result)
```

This Python function, `rolling_max`, takes a list of integers as input and generates a new list with the maximum element found in each rolling window of the input sequence. The function uses the formula `max(n, m)` to find the maximum element, where `m` is the maximum found so far, and `n` is the current element.

The function then returns the new list with the maximum element found in each rolling window. 

This script tests the function with three different sets of numbers, and prints the results to the console.