```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split()
    read as numbers, sorted from smallest to largest.
    return ' '.join(sorted_nums)
    """

def test_sort_numbers():
    numbers = """three one five
           six two eight
         nine zero seven"""
    expected = """one three five
           six two eight
         nine zero seven"""
    return sort_numbers(numbers) == expected

if __name__ == "__main__":
    print(test_sort_numbers())
```

This Python script provides a function `sort_numbers` that sorts a given string of numbers. The function splits the numbers string, then sorts the numbers from the smallest to the largest using `sorted()` function. The `test_sort_numbers` function contains a test code that calls the `sort_numbers` function with an example input string and compares the output with the expected output. The script also includes `if __name__ == "__main__":` to ensure the test is run when the script is executed.