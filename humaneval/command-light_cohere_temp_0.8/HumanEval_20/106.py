```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    numbers.sort()
    sorted(numbers, key=lambda n: math.abs(n))
    return (numbers[0], numbers[1])
```
The function takes a list of numbers as an argument and sorts the list based on the absolute values of the elements. The function then returns the two elements that are the closest to each other, and returns them in order (smaller number, larger number).

This function can be used to find the closest elements in a list of numbers. You can test this expected output by calling the function with your desired list of numbers as an argument.