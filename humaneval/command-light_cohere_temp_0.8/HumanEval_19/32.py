```python
from typing import List
def sort_numbers(input_str: str) -> str:
    """ Sorts space-delimited string of numbers from zero to nine.
    Valid choices are following 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
    numbers = [int(n) for n in input_str.split()]
    example,numbers: [3,1,5]
    in order: [1,3,5]
    numbers.sort() 
    # Return in ascending order.
    numbers_sorted = ','.join(sorted(numbers))
    return numbers_sorted

# Example tests
def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'

test_sort_numbers()
```
This Python script defines a function called `sort_numbers` that sorts a space-delimited string of numbers. The function first splits the numbers from the input string into a list, and then uses the sorted() method to sort the numbers in ascending order. The function then joins the numbers in the sorted list into a string and returns it. 

The `test_sort_numbers` function tests the `sort_numbers` function with an example input string.