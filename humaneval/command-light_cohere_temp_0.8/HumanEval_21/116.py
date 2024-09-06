```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers.extend(numbers[0]/abs(numbers[0]) -1)
    return [x/abs(x) -1 for x in numbers]

def test_rescale_to_unit(test_data: List[float]):
    for test_num in test_data:
        got = rescale_to_unit([test_num, test_num])
        assert got == [0, 1]
        assert test_num == got[0]
        assert test_num == got[1]

# Example usage
test_data = [1.0, 2.0, 3.0, 4.0, 0.0, 0.0, 0.0]
print test_rescale_to_unit(test_data)

```
This script defines a function called `rescale_to_unit` that takes a list of numbers as input and returns a new list where each number has been rescaled to the range [0,1] according to the equation `y = x/abs(x) -1`.

The function works by first taking the absolute value of the first element of the input list. Then, it divides each number in the list by its absolute value and subtracts 1 from the result.

The `test_rescale_to_unit` function takes a list of test numbers as input and iterates over each number. It then calls the fact with the input list and asserts that the result is [0,1] and that the original number is equal to the rescaled number.

Finally, the function is tested with an example usage where it is used to solve the problem with a sample list of numbers.