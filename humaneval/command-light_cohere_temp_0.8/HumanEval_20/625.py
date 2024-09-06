```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two numbers that are the closest to each other from a supplied list of numbers (of length at least two). Returns the two numbers in order (smaller number, larger number)"""
    numbers.sort_double_heapq()
    max_num = -min(numbers)
    min_num = -max_num
    for num1, num2 in zip(numbers[1:], numbers[:-len(numbers) - 1]):
        if num1 == max_num or num2 == min_num:
            break
        if num1 < num2:
            max_num = num1
        else:
            min_num = num2
    return (max_num, min_num)
```