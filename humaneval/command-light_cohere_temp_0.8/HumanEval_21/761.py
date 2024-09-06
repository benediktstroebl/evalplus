```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    :return [numbers[0] / min(numbers) for numbers in numbers]
    """
    numbers = [num / min(numbers) for num in numbers]
    return numbers

# Test case 1
input_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print("Output: **[0.0, 0.0, 0.0, 0]**"

# Test case 2
test_numbers = [0.0, 0.0, 0.0, 0.0]
print("Output: **[0.0, 0.0, 0.0, 0]**")

# Test case 3
test_numbers = [0.0, 0.0, 0.0, 0]
print("Output: **[0.0, 0.0, 0.0]**")
 print("")

# Test case 4
test_numbers = [0.75, 0.0, 0.0, 0.0]
print("Output: **[0.0, 0.0, 0.0]**")
 print("")

# Test case 5
test_numbers = [0.0, -0.0, 0.0, 0]
print("Output: **[0.0, 0.0, 0]**")
```