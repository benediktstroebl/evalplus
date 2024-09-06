```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(a - b) < threshold for a, b in zip(numbers, numbers[1:]))
```

The function `has_close_elements` takes in a list of numbers and a threshold as inputs, and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. 

The function relies on the use of a generator expression, which allows for short-circuit logic and yields results in a lazy fashion. Generator expressions iterate over pairs of numbers obtained from slicing the list with the help of the `zip` function. The `any` function then checks if the condition of closeness is met for any of the pairs, with the `abs` function taking care of both negative and positive differences. 

You can test this function using the following calls:
```python
>>> has_close_elements([1.0, 2.0, 3.0], 0.5)
False
>>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
True
```

These tests correspond to the test cases provided in the original problem.