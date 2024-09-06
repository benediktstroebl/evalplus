Here is a Python script that contains a self-contained function that solves the problem:
```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    """
    <|—"

    # Sort the numbers
    sorted_numbers = sorted(numbers)

    # The two closest numbers
    first_number = sorted_numbers[0]
    second_number = sorted_numbers[1]

    # Return them in order of the smaller number
    return first_number, second_number
```
This code uses the 'typing' module to incorporate type hints into the function definition. This not only improves code readability but also helps the function to be executed with the correct arguments without the need for additional type-checking.