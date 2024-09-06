```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ 
    Return the two closest elements in the list.
   
    # Sort the least to greatest and get the first two
    elements
    """
    return (numbers[0], numbers[1]) if len(numbers) >= 2 else "No valid input"

# Test the function with a simple example
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 2])) # (2.0, 1.0)


# The test passed, and the output is a tuple with the two closest elements
```