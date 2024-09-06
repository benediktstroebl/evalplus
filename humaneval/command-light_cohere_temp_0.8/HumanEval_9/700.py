```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = List(sorted(numbers))  # Convert list to sorted order
    return [x for x in numbers if x == numbers[-1]]  # Return the rolling maximum element
test_data = [2, 3, 3, 2, 1]
result = rolling_max(test_data)
assert len(result) == 4, "The length of result is incorrect"
assert result == [2, 3, 3, 3], "The rolling maximum elements are incorrect"
``` 
This Python code defines a function called rolling_max that takes a list of integers as input and returns a new list containing the rolling maximum elements found within the input list. It uses the provided test_data list as a sample to test the correctness of the rolling_max function, and the output is compared against the expected result.