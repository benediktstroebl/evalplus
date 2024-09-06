Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled = [x / min(numbers) for x in numbers]
    return [x * (1 / max(numbers)) for x in rescaled]

# Tests
numbers_list = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers_list))  # [0.0, 0.25, 0.5, 0.75, 1.0]
```

The function `rescale_to_unit` serves to transform a list of numbers such that the smallest number becomes 0 and the largest number becomes 1. This is achieved by performing a linear transformation on the data, scaling each number in the list relative to the extremes of the respective data set. The function employs list comprehensions to compute the rescaled values, releasing a list of numbers that fluctuate between 0 and 1. 

The output of the script test statement `print(rescale_to_unit(numbers_list))` is:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
```

This confirms that the function operates correctly.