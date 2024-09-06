Here is the solution:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Returns a tuple containing the two numbers with the smallest and largest values from the list.
    """return sorted((num1, num2), key=lambda num: num)[:-2], -1)
```

This script defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two numbers with the smallest and largest values. The script uses the sorted function to order the numbers based on their values, and then uses the slice notation to only select the first two elements of the sorted list.