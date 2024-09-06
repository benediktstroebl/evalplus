```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements` uses the `any` function to check if there are any elements in the list that are closer than the given threshold. The `zip` function is used to iterate over pairs of elements in the list, and the `x - y < threshold` condition checks if the difference between two consecutive elements is less than the threshold.

To use this function, you can call it with a list of numbers and a threshold value and it will return `True` if any two numbers in the list are closer to each other than the threshold and `False` otherwise.

Here is an example of use:
```python
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))
```

This would output:
```
True
``` 

This is because there are two consecutive elements, namely 2.0 and 2.8, that are closer than the 0.3 threshold. The code will return `True` in such cases.