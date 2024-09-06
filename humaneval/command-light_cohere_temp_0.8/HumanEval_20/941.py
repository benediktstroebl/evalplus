```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)

    # Create tuples containing the two closest elements and their corresponding distances
    closest_pair = (min(numbers), max(numbers))[0], max(numbers) - min(numbers)[0])
    return closest_pair
```
The function `find_closest_elements` takes a list of numbers as input and returns a tuple containing the two closest elements along with their distance. The script is a implementation of this function is straightforward and follows the logic of finding the two closest elements in a list of numbers.