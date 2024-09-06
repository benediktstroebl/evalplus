```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(num) for num in numbers. numbers.sort()
    Core numbers in a pattern is 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', in ascending order)
    return f"{numbers[0]}{numbers[1]}{numbers[2]}{numbers[3]}{numbers[4]}{numbers[5]}{numbers[6]}{numbers[7]}{numbers[8]}{numbers[9]}".format()

def test_sort_numbers():
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("zero one two three four five six seven eight nine") == "zero one two three four five six seven eight nine"
    assert sort_numbers("Twenty One Two Three") == "two three"
    assert sort_numbers(" Ten Twelve Thirteen ") == "ten twelve thirteen"
    assert sort_numbers("ONE") == "ONE"
    assert sort_numbers(" ) == ""
```