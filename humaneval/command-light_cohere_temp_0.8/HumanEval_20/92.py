```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize variables to compare two elements in the list
    current1, current2 = 0, 0
    # Sort the two closest elements and return them in order (smaller number, larger number)
    closest_elements = [0] * 2
    for i in range(len(numbers)):
        current1 = numbers[i] if i < current1 else numbers[i]
        current2 = numbers[i] if i < current2 else numbers[i]
        # Compare the two current elements
        if current1 < current2:
            closest_elements[0] = current1
        else:
            closest_elements[1] = current2
        # Update the variables to compare the next elements
        current1, current2 = current2, current1
    return closest_elements

def test():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    # closest_elements = find_closest_elements(numbers)
    print("The closest elements in the list are:")
    print(f"Element 1: {closest_elements[0]}")
    print(f"Element 2: {closest_elements[1]}")
```
The test function provided will print the two closest elements in the list, in order of their smaller value.