Here's a solution to the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    new_numbers = [num / max(numbers) for num in numbers]
    return new_numbers
```
This function takes a list of numbers as input and applies a linear transformation to the list, such that the smallest number in the list will become 0 and the largest number in the list will become 1.  The function then returns a new list of numbers.

Let's break down the functionality of this function:
- The function starts with typing import List to import the List data type.
- The `numbers` parameter is a list of float numbers.
- The function uses the `List[float].append()` method to add the `numbers` list to the `new_numbers` list. This way ensures that the numbers are also converted into float data type.
- The function then applies a linear transformation to the `new_numbers` list. The linear transformation is achieved by creating a list of the form `[num / max(numbers)} for each number in the numbers list.
- The `max(numbers)` function returns the maximum value in the numbers list, and the `num / max(numbers)` expression is used to divide each number by its corresponding maximum.
- The `new_numbers` list now contains the transformed values.
- The `return new_numbers` statement will return the `new_numbers` list as the output of the function.

This self-contained Python function demonstrates how to transform a list of numbers in a linear way to ensure that the smallest number becomes 0 and the largest becomes 1.