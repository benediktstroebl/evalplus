```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # sort the list ascending
    numbers.sort()
   
    sort = [num for num in numbers if num < threshold] + [num for num in numbers if num > threshold]
    # check if two numbers are equal, they are close to each other
    for i in range(len(sort) - 1):
        if sort[i] == sort[i + 1]:
            return True
    return False

# Test the function
numbers = [1.0, 2.8, 3.8, 4.8, 5.0, 6.8, 5.0, 0.0, 8.8, 1.8]

result = has_close_elements(numbers, 0.8)  # False

print(has_close_elements(numbers, 0.8))
```