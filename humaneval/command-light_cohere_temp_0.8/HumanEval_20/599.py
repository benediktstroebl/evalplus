```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    numbers.sort()
    sort(numbers, key=lambda x: x[0]))
    return (numbers[0], numbers[1])
```
This function takes a list of numbers as input and sorts them based on the first element. It then returns a pair of the two numbers that are closest to each other.