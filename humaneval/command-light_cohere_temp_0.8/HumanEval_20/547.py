```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Select two elements in the list that are closest to each other
    a, b = min(numbers[::i], numbers[::j])
    i, j = 0, 1
    while i < len(numbers) - 1 and j < len(numbers) - 1:
        if numbers[i] < a and numbers[j] < b:
            a, b = numbers[i], numbers[j]
        i += 1
        j += 1
    return a, b
```
This function takes a list of numbers as input and returns a tuple containing the two closest elements in the list, in order of the smaller number. The function uses a mathematical operation min to find the smallest number between two elements in the list. The loop continues until the smallest of the two elements is found, or until the end of the list is reached.