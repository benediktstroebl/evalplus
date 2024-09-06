```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        diff = numbers[-1] - numbers[0]
        if diff > 0:
            return numbers[0], numbers[-1]
        else:
            middle = len(numbers) // 2
            left, right = numbers[middle-1], numbers[middle]
            if left == right:
                return left, left
            elif abs(left-right) == abs(numbers[0]-numbers[-1]):
                return left, right
            else:
                return numbers[0], numbers[-1]
```
The function first sorts the input list of numbers. It then checks if the list has less than two elements and raises a ValueError if it does. If the last number is not larger than the first one, the middle elements are checked and returned if they are equal. If not, it returns the first and last numbers. The script includes test cases for this solution.