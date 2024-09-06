Here's a solution:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply the linear transform
    numbers = [x / 100.0 for x in numbers]
    return numbers

# Example usage
input_list = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers = rescale_to_unit(input_list)

# Output:
[0.0, 0.0, 0, 0.0]

This solution uses the rescaling technique, where we divide each number in the list by 100.0 and then divide by this, which causes the numbers to be scaled between 0 and 1. The function can be used to test this technique easily.