```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine,
    Valid choices are zero, one, two, three, four, five, six, seven, eight and nine.
    Numbers are sorted in ascending order
    """
    return numbers.split()
        strings in the numbers

def test_sort_numbers() -> None:
    numbers = "three one five six seven eight nine"
    sorted_nums = sort_numbers(numbers)
    print(sorted_nums)
    return

#run the tests
test_sort_numbers()
 ```