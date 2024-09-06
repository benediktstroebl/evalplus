```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    # Select two elements that are the closest to each other
    a,b = numbers[0]
    while numbers[1:]:
      if numbers[0] > numbers[1]:
          a,b = numbers[1],numbers[0]
      else:
          break
    # Return the two closest numbers
    return (a,b)

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
result = find_closest_elements(numbers)
```

The provided code defines a function `find_closest_elements` that aims to find and return the two elements in a list of numbers that are the closest to each other. The code then proceeds to sort the list, and then, using a loop, compares each number in the list with the first to find the smallest one. Finally, it returns the smallest number and the larger number.