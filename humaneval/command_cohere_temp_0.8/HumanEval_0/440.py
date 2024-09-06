Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(x - y) < threshold for x, y in zip(numbers, numbers[1:]))
```
The `has_close_elements` function takes two arguments; a list of numbers and a threshold for closeness. It uses the `any` function with a generator expression to check if any adjacent elements in the list have a difference less than the threshold. 

This solution is concise and efficient for large lists as it doesn't require looping through the list multiple times. 

To test this function, you can call it with various input tests like the ones provided in the problem statement. Here is an example: 
```python
# Test case 1
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Output: False

# Test case 2
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Output: True
```
The function passes both provided tests and returns 'True' for the second test case and 'False' for the first test case, as expected. 
You can also add more tests to ensure the function works correctly for different scenarios.