```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number)
    """
    if len(numbers) < 2:
        return numbers
    
    first, second = (numbers[0] , numbers[1])
    for num in numbers[2:]:
        d = num - first
        a = (second - first) / d
        if a < 0:
            first = num
            second = first
        elif a > 0:
            second = num
    return (first, second)
``` 
This function takes a list of numbers as an input and returns a tuple containing the two numbers that are closest to each other. The function works by finding the two closest numbers in the list and then compares them to each other. The first element is the larger number, and the second element is the smaller number. This process continues until the result is a tuple containing two elements.