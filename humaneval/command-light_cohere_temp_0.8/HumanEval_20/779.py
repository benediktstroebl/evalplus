Here is a Python script that contains a self-contained function that solves the problem:
```python
from typing import List, Tuple
def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(key=lambda n: -n)
    # Create a tuple with the first element of the sorted list and the second element
    return (numbers[0], numbers[1])
```

This function takes a list of numbers as an argument. It sorts the list and returns a tuple with the first element of the sorted list and the second element. This makes the tuple the first element the closest element and the second element is the second closest element. The returned tuple is then returned.