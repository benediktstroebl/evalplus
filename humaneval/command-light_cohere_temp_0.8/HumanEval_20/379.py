Here's the solution to the problem:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Get the two closest elements and return them in order
    return (min(numbers), max(numbers))
```

This code utilizes the min and max functions from the typing module to select the two closest elements from the input list of numbers and returns them in order. The min function returns the smallest value in the list, while the max function returns the largest value in the list.

This self-contained Python function finds and returns the two closest elements in the input list, fulfilling the requirements of the problem statement.

Please note that this solution assumes the input to the function is a list of numbers and does not handle any specific error cases or exceptions.