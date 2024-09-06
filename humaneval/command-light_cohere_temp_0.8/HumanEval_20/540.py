```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # sort list of numbers in ascending order
    sorted_numbers = sorted(numbers)

    # find the first and second element of the sorted list
    first_element = sorted_numbers[0]
    second_element = sorted_numbers[1]

    return first_element, second_element

# Example
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)

print(result)
```
This script defines a function called `find_closest_elements`, which takes a list of numbers as an argument and returns a tuple containing the two closest elements from the list. The function first sorts the list of numbers in ascending order using the `sorted` function, and then finds the first and second elements of the sorted list. The function then returns these first and second elements in that order, and the result is a tuple containing the two closest elements.

The example usage demonstrates how to call the function with a list of numbers and print the result, which will be the two closest elements from the list.