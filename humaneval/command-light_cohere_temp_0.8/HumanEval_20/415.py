Here's a Python script that solves the problem:

```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least 2), select and return two that are the closest to each other and return them in order (smaller number, larger number).
    
    :return (smallest, largest)
number_pair = sorted(zip(*numbers), key=lambda x:x[0])[0]
    return (number_pair[0], number_pair[1])
```
The test code will be:

```python
from typing import List
from typing import Tuple

def test_find_closest_elements(numbers: List[1.0, 2.0, 3.0, 4.2, 5, 6, 7):
    expected = (2.0, 3.2)
test_find_closest_elements(numbers) == expected
```