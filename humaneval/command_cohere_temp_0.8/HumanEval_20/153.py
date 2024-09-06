```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        diff = numbers[-1] - numbers[0]
        if abs(diff) < 1e-5:
            return (numbers[0], numbers[0])
        else:
            return (numbers[0], numbers[-1])
```
The function sorts the input list of numbers and checks if the list has at least two elements. It then determines whether the list's two elements are close enough to each other, considering the spacing between them. If they are, the function returns both elements, each repeated once. Otherwise, it returns the first and last numbers after sorting. The function handles some edge cases but could benefit from additional testing and possibly error message handling.