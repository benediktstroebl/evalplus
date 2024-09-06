```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # initializing numbers from [1.0, 2.0, 3.0, 4.0] to [0.0, 1.0, 0]
   0]
    # Applying linear transform to the numbers
    numbers = [num / max(numbers) for num in numbers]
    # returning the new numbers
    return numbers

# Test cases
test_cases = [
    [ [1.0, 2.0, 3.0, 4.0],
   0], [0.75, 1.0]
# Output: [0.0, 0.0, 0.0, 0]

test_cases = [
    [1.0, 2.0, 3.0, 4.0],
   0, [0.75, 1.0]
# Output: [0.0, 0.0, 0, 0]

# The solution using the function
rescale_to_unit
print(rescale_to_unit(test_cases))
```
This Python script defines a function called `rescale_to_unit` that takes a list of numbers as an argument and applies a linear transformation to the list, such that the smallest number becomes 0 and the largest becomes 1. The function then returns the list of new numbers. The script also includes a set of test cases, which are a list of lists containing pairs of numbers. These test are then used to test the `rescale_to_unit` function by passing the test cases and printing the results.