```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two elements that are the closest to each other and returns them in order (smaller number, larger number)"""
    closest1, closest2 = float('inf'), float('-inf')
    for num1, num2 in zip(numbers, numbers[1:]):
        diff = num1 - num2
        if diff < closest1:
            closest1, closest2 = num1, num2
        elif diff > closest2:
            closest1, closest2 = num2, num1
    return closest1, closest2
```
This script defines a function `find_closest_elements` that takes a list of numbers and returns a tuple containing the two closest numbers in order. It uses a method `zip` to iterate through the list twice and calculates the difference between each pair of numbers. The results are stored in variables `closest1` and `closest2`. If the difference is smaller than `closest1`, the variables are updated to the first number. If the difference is larger than `closest2`, the variables are updated to the second number. This process continues until theta pair of numbers is found that satisfies the condition.