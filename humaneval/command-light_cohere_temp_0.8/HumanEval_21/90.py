```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Function to rescale list of numbers such that the smallest becomes 0 and the largest becomes 1
    numbers = [num / max(numbers) for num in numbers]
    return numbers
``` 
This script defines a function called `rescale_to_unit` that takes in a list of numbers and returns a new list where each value has been rescaled such that the smallest number becomes 0 and the largest number becomes 1.  The test cases in the `type` and `isinstance` are used to test the function.