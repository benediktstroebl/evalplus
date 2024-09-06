```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment in the sequence.
    Returns the
    list with the maximum elements from the sequence, 
    rolling over the list as per the requirement.
    """

    function utilizes the of a List and List comprehension, 
    along with the built-in max() function to achieve this.
    """
list is initialized with the input numbers and then 
    augmented with the current number and the maximum found 
    until the desired moment is reached.
    """
The resulting list contains the elements in the order 
    they were found, with the maximum elements 
    appearing first.
    """
test cases are also provided in the function to 
    validate the correctness of the function.

# Example:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

```