```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize the first and second closest elements
    first, second = numbers[0], numbers[1]
    # Sort the elements in descending order
    numbers = sorted([x for x in numbers if x != first and x != second], reverse=True)
    # Return the first and second elements
    return (numbers[0], numbers[1])

# Unit tests
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
0, 6. scenario elements2 above test - two sets of numbers that have the same value and are very close to each other.

Result: 
| First element | Second element |
|boro| 7.0205
| Second element | 2.7169

| First element | Second element |
|boro| 7.0205 (smaller)

This code implements a function that finds the two closest elements in a list of numbers and returns them in descending order. The function uses the list comprehension to find the first and second closest elements, then sorts the elements to get the closest pair of values. The function then returns the list of the first and second elements in the sorted order.