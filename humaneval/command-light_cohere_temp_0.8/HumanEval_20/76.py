```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    two closest elements and their order.
    numbers = sorted(numbers, reverse=True)  # sorts the list of numbers in descending order
    min_num = min(numbers)  # finds the smallest number in the list
    max_num = max(numbers)  # finds the largest number in the list
    closest_num = min_num if min_num < max_num else max_num  # finds the smallest or largest number that is closest to the other
    closest_elements = (min_num, max_num)  # creates a tuple with the two closest numbers
    return closest_elements
```
This function takes a list of numbers and returns a tuple with the two numbers that are closest to each other and in order (smaller number, larger number).

This solution uses the Python 'typing' module. The function returns a number of the list of floats and sorts the list in descending order. The list is then the smallest number using the 'min' function and the largest number using the 'max' function. Then, the function finds the smallest or largest number that is closest to the other using a boolean expression. The function creates a tuple with the two closest numbers and returns it.