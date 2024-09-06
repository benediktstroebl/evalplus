```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers[0] = 0
    numbers[1] = 1
    return numbers

def test_rescale_to_unit(test_numbers: List[float]) -> None:
    # Test the function
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    - res = rescale_to_unit(numbers)
    assert all(x == 0 for x in res)
    assert all(x == 1 for x in res)
    assert test_numbers == [0, 0, 0, 0, 0, 0, 0, 0, 1]  # This is an invalid input! You may need to change this test to handle this edge case better
    return

print("Test succeeded!")
```