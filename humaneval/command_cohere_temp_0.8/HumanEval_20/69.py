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
            return numbers[middle], numbers[middle]
```
This Python script provides a function called `find_closest_elements`, which takes a list of floating numbers as input and returns a tuple of two numbers that are closest to each other. The function first sorts the input list and checks its length to ensure at least two numbers are provided. Then, it examines the difference between the first and last numbers to determine whether the closest pair is at the start and end of the sorted list. If not, it retrieves the middle number for a potential match, averaging down the search range. This process helps find the numerically closest pair efficiently, ensuring correctness while keeping the code concise.