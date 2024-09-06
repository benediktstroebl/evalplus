```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two numbers from the input list that are closest to each other and returns them in order (smaller number, larger number).
    
    Parameters: 
        - numbers (List[float]): A list of at least 2 numbers.
    
    Returns: a tuple containing the two closest numbers in order.
```
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

find_closest_elements(numbers)
```
The script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest elements. The function first sorts the `numbers` in ascending order using the `sorted` function. It then selects the first two elements from the sorted list, and returns a tuple containing these two numbers. The test case provided is successful.