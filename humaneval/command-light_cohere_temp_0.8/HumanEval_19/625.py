```python
import stringIO
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split()
    validity_ if all the
numbers = [int(num) for num in numbers.split()]
    numbers = sorted(numbers, reverse=True)
    return numbers

def test_sort_numbers():
    numbers = ['three one five', 'two three four', 'six seven eight', 'nine']
    expected = ['one', 'three', 'five']
    return sorted(numbers), expected

if __name__ == "__main__":
    input = stringIO.readline()
    check = test_sort_numbers()
    print(check)
```

The function `sort_numbers` takes a string of numbers as input and returns a sorted version of that string. The function first splits the string into individual numbers and stores them in a list. Then, it sorts this list of numbers from smallest to largest using the `sorted` function and returns it. The `test_sort_numbers` function is used to test the `sort_numbers` function.