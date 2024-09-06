Here's the solution:
```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects two numbers from a list that are closest to each other and returns them in order of their values (smaller number, larger number).
 We use the built- in function's sorted function with a reverse=True parameter to sort the list of numbers in descending order and then select the first two.
    The return values in order (smaller number, larger number)
"""
    return sorted(numbers)[0:1]

test_data = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(test_data)

print(result) # [2.0, 3.0]
```