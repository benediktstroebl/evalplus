Here's the Python script with the self-contained function:
```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Apply a linear transform to the numbers in the list, such that the smallest number will become 0 and the largest will become 1
    new_numbers = [x / 100.0 for x in numbers]
    return new_numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
result = rescale_to_unit(numbers)

# Test cases
def test_rescale_to_unit():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0.0]) == [expected numbers
   
def test_rescale_to_unit2():
    assert rescale_to_unit([0.75, 0, 0]) == [0.0, 0.0, 0] == [0, 0, 0]

def test_rescale_to_unit3():
    assert rescale_to_unit([0.0, 0, 0]) == [0, 0, 0]

# Test suite
test_rescale_to_unit.add_to_tests(test_rescale_to_unit, test_rescale_to_unit2, test_rescale_to_unit3)

Please use this script to test your function and add the test cases.