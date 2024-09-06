Here is a Python script that includes a self-contained function that solves the problem you have described:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided.")
    min1, min2 = numbers[0], numbers[1]
    closest = min1 if min1 < min2 else min2
    return (min1, closest)
```
This function takes a list of numbers as input and uses the first two elements of the list to determine the two closest elements, then returns them in order. 

Let me know if I can assist you with anything else you would like to do or discuss!