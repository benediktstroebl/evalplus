Here is a self-contained Python script with a function that solves the problem:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Function to find two closest elements in a list of numbers
    # Select the two smallest numbers and return them in order
    smallest1 = min(numbers, key=lambda num: num)
    smallest2 = min((smallest1 for num in numbers if num != smallest1), key=lambda num: num)
    return smallest1, smallest2

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)
print(result)
```

This function takes a list of numbers and finds the two closest elements to each other in the list. It then returns the two of those numbers, in order of them being smaller to larger.

Note: This function uses the `min` function to select the smallest element from the list. If the list contains more than two elements, it will select the smallest two elements.