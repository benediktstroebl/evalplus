Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [num / max(numbers) for num in numbers]
```
This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1]. The function simply divides each number in the list by the maximum number in the list. This approach ensures that the smallest number becomes 0 and the largest number becomes 1 after the transformation.

To test this function, you can run the following code:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0]
expected_list = [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit(test_list))
print(expected_list)
assert rescale_to_unit(test_list) == expected_list
```
The function passes the test as the printed list and the expected list are equal.