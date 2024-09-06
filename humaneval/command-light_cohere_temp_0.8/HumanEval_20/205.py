```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Find two numbers that are closest to each other and return them in order (smaller number, larger number).
    If the list has at least two numbers, it uses the `distances` function to calculate the distance between each pair of numbers in the list, and then sorts them by the calculated distance, ensuring that the smaller number comes first.
    Then two numbers that have the smallest distance, and returns them in order.
```