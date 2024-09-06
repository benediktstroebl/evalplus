```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(key=lambda x: -x)
    # Select the two closest elements
    _, smaller = min(numbers), key=lambda x: x)
    _, larger = max(numbers), key=lambda x: x)
    return smaller, larger
```
The code defines a function named find_closest_elements that takes a list of numbers as input and returns a tuple of the two closest elements in the list, along with their relative order. 
The code then sorts the list of numbers using the key parameter with a lambda function that returns -x for each number. Then, it selects the two closest elements using the min and max functions with the key parameter that returns the corresponding number. Finally, it returns the smallest and largest numbers in the list.