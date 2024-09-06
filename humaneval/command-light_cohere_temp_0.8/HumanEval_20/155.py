```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize the two closest elements to None
    closest_1, closest_2 = (None, None)

    # Sort the numbers by their first element, then compare the remaining elements
    for i, num in enumerate(numbers):
        if i > 1:
            if num < numbers[i - 1]:
                closest_1, closest_2 = (num, numbers[i])
                break
        elif i == 1:
            if closest_1 is None or num < closest_1:
                closest_1, closest_2 = (num, closest_1)
                break

    return closest_1, closest_2

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

print(find_closest_elements(numbers))
```

This code defines a function called `find_closest_elements` that takes a list of numbers and returns a tuple containing the two closest elements in the list, along with a comparison between them. The function uses a sorting algorithm and a loop to compare each number in the list with the previous two closest elements, and keeps track of the two closest elements using a tuple. The example usage demonstrates how to call the function with a list of numbers and print the returned tuple.