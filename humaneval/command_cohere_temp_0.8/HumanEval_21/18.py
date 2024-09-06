Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the largest and smallest values in the input list. This approach uses list comprehension and primitive Python operations only, which may be desirable for simple problems like this one.

To test this function, you can use the following code:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0]
expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]

assert rescale_to_unit(test_list) == expected_result
```

The function should return the expected result [0.0, 0.25, 0.5, 0.75, 1.0] for the input test_list.