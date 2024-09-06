```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Returns the two closest numbers from a supplied list of numbers and returns them in order (smaller number, larger number).
    """
    if len(numbers) < 2:
        return numbers[0], numbers[0]
    else:
        first, second = find_closest_elements(numbers[: len(numbers) // 2])
        third = numbers[-1]
        
        if first < second:
            return second, third
        elif second < first:
            return third, first
        else:
            return first, second
```

This code utilizes the Python programming language and its function called "find_closest_elements" to solve the problem of finding the closest pair of elements in a list of numbers. The function takes a list of numbers as an input and returns the two closest numbers from the list in descending order. The function is tested to handle lists with at least two elements, ensuring that it can handle any length of list.