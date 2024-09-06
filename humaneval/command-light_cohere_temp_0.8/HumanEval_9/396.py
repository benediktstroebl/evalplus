Here is a Python script that solves the markdown code block problem:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    result = [max_so_far]
    
    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        result.append(max_so_far)
    
    return result

# Test case:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```
This code uses the `rolling_max` function to solve the given problem. The provided test case is used to pass the test with the function. The `rolling_max` function takes a list of integers as input and returns a list of the maximum elements found in that list, calculated by the rolling window approach.