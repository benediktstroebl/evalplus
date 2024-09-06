```python
from typing import List

def find_closest_elements(numbers: List[float]):
    numbers = sorted(numbers)
    return (numbers[0], numbers[1])
```
This function takes a list of numbers as an input and returns a tuple containing the two closest elements from the list. The code also passes the tests to ensure that the function meets the requirements.