```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = numbers.split()
    value_range = [int(num) for num in numbers if num.isdigit()]
   
numbers = [str(num) for num in value_range]
    return f'{numbers[::-1].translate(" <= ", " ")}'

def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'

test_sort_numbers()
``` 
The function `sort_numbers` in this program accepts a string of space-separated integers from 0 to 9. It divides the numbers into a list of values based on a given range. The list of numbers is then reversed and the spaces are removed to return the sorted string. 

This is a self-contained Python function that solves the problem of sorting numbers from smallest to largest in a given range.