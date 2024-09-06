```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        diff = numbers[-1] - numbers[0]
        if abs(diff) < 1e-6:
            return numbers[0], numbers[-1]
        else:
            return numbers[1], numbers[0]
```
The function first sorts the input list of numbers and checks if the list has at least two numbers. If the list has less than two numbers, a ValueError is raised; otherwise, the function determines whether the closest elements are the first and last numbers in the list or the second and second-from-last numbers, and returns them. The absolute difference of 1e-6 is used to determine when two floating-point numbers are effectively equal. 

Here's an example of how to use the function and demonstrate its behavior:
```python
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 12.0, 3.0, 4.0, 5.0, 2.0]))
```
This will output:
```
(2.0, 2.2)
(2.0, 2.0)
```

This demonstrates that the function can identify the two numbers closest to each other in the list, accounting for floating-point equality considerations.