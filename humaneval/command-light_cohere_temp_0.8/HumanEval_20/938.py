Here is a self-contained Python script that solves the problem:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")
    else:
        numbers.start = min(numbers)
        end = max(numbers)
        while start != end:
            mid = (start + end) // 2
            if numbers[mid] < numbers[start]:
                start = mid
            else:
                end = mid
        return start, end
```

This function takes a list of numbers and returns a tuple of the closest elements. It checks the validity of the input list, ensuring it has at least two elements, and then uses the `min()` and `max()` functions to find the minimum and maximum values. The function then repeatedly calculates the halfway numbers and checks which one is smaller than the start and the other is larger than the start. This process continues until the start and end are the same, at which point it stops and returns the start and end values.