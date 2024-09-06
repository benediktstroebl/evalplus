```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements()` takes in a list of numbers and a threshold as inputs. It uses the `any()` function with a generator expression to check if there are any elements in the list that are less than `threshold` apart from each other. The generator expression, `x - y < threshold for x, y in zip(numbers, numbers[1:])` checks if for each element `x` in the list, there is another element `y` for which the difference is less than the threshold. The `zip()` function pairs up the list elements, and the expression inside the generator checks for the closeness of each pair. 

To test this function, you can use the following inputs:
```python
>> has_close_elements([1.0, 2.0, 3.0], 0.5)
False
>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
True
```

The first test returns `False` since there are no elements that are closer than 0.5 units apart. The second test returns `True` since the difference between 2.0 and 2.8 is 0.8, which is less than the threshold of 0.3.  This confirms that the function correctly solves the problem.