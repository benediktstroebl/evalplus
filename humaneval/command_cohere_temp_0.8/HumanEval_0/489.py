```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements` takes in a list of floats and a threshold as parameters, and returns a boolean value. It uses the `any` function to check if there exists two elements in the list that are less than the threshold of each other when taken as absolute differences. 
The above solution assumes that the list contains at least two elements.