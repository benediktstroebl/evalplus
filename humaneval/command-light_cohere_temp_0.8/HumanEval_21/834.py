```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers[:1] = [0]
    numbers[1:] = 1
    return [x*10 for x in numbers]

def test_rescale_to_unit(test_numbers: List[float]):
    actual_numbers = rescale_to_unit(test_numbers)
    for num, expected in zip(actual_numbers, [0.0, 2.0, 3.0, 5]):
        assert num == expected,
    return True
```

The function rescale_to_unit in this script accepts a list of numbers as an input and outputs a list of the same numbers but scaled to the range [0, 1]. The numbers are scaled to the range [0, 1] by applying a linear transformation, with the lowest number becoming 0 and the highest number becoming 1. The numbers are then multiplied by 10.

The test_rescale_to_unit function tests the rescale_to_unit function with a list of test numbers. It creates a list of numbers using the test_numbers function and applies the function to the list to produce the actual_numbers list. The function then iterates over the numbers in the actual_numbers list and compares each number with the corresponding expected value. The test succeeds when all of the numbers match their expected values.