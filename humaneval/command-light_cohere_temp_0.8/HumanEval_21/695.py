Here is a self-contained Python script with a function that solves the problem you've outlined:
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    # Calculate the difference between the smallest and the largest element
    diff = min(numbers) - max(numbers) + 1
    # Calculate the linear transformation based on the difference calculated
    transform = [0.0] + diff / (len(diff) - 1)
    # Apply the linear transformation to the numbers in the list
    numbers = [num * transform[idx] for idx, num in enumerate(numbers)]
    return numbers


# Test the function with various input values
test_cases = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 1.0, 2.0], 2.0],
   0
0]

# Test the function with the input list of numbers
test_numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 0.0]
# 
test_cases


for test_case in test_numbers:
    actual_result = rescale_to_unit(test_case)
    print(f"Test case: {test_case} => {actual_result}")
    print("="*)"
```
This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where each element has been rescaled to the range [0, 1]. The function first calculates the difference between the smallest and the largest element in the input list. It then calculates the specific linear transformation based on that difference. Finally, it applies the transformation to the original numbers and returns the result.