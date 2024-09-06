```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return sorted(set(nums))

def test_sort_numbers():
    return sort_numbers('three one five') == 'one three five'

if __name__ == "__main__":
    print(test_sort_numbers())
``` 
This code defines a function sort_numbers that sorts a string of numbers according to their values. The function utilizes theator-set method with a set of numbers to sort them in ascending order. The test_sort_numbers function tests the correctness of the sort_numbers function by comparing the output with the expected sorted result.