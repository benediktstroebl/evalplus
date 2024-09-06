```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    If any two elements are closer than the threshold, return True
    Otherwise, return False
    """
    return any(x <= threshold for x in numbers) == False

# Test the function with markdown code block
# The first argument is the list of numbers
# The second argument is the threshold

# > has_close_elements([1.0, 2.0, 3.0], 0.5)
 - "Note that 1.0 and 2.0 are not closer to each other. 

# Output: True, since all the elements are less than 0.5

# Output:
True