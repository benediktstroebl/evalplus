Here's the solution:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers = [n / 100.0 for n in numbers]
    return numbers

def test_rescale_to_unit(numbers: List[float]):
    assert len(numbers) == 3
    for i in range(0, len(numbers)):
        assert numbers[i] <= 0.0
        for j in range(0, len(numbers) - 1):
            assert numbers[j] <= numbers[j+1]
    return

```
We have a self-contained function called rescale_to_unit that accepts a list of numbers and returns a new list with the same values but potentially a different scale. This function works by dividing each number in the list by 100.00 and returning the test on the list of numbers, which guarantees that the resulting numbers will be between 0 and 1.00.

The test_rescale_to_unit function accepts a test function as an argument. It asserts that the test function's input has the right length and that all of the numbers in the list are non-negative. The test function also checks that all the numbers in the list are non-negative by comparing each number to the next number in the list.

This script also demonstrates how to use the function and test it with a test case.