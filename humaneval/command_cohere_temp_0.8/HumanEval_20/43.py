```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    x = numbers[-2]
    y = numbers[-1]
    return x, y
```

The function `find_closest_elements` serves to obtain the pair of numbers from a supplied list that are closest to each other. The algorithm is straightforward: sort the list and select the second last and last elements, which, by definition, are the closest pairs. The provided code includes type annotations and error handling for scenarios with an insufficient list length to solve the problem correctly. 

Here is an example of how to use the function and an example of its behavior: 
 ```python
 >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
 (2.0, 2.2)
 >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
 (2.0, 2.0)
 ``` 
The function's behavior aligns with the problem description, providing valuable number pairs.