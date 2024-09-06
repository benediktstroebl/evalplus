```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are numbers from 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    # Convert input string to list
    numbers_list = list(numbers)
    # Sort the numbers from smallest to largest
    numbers_list.sort()
    recenter smallest numbers first.
    # Join strings with numbers, all others
    numbers_list = list(numbers_map[numbers_list])
    # Return the sorted string
    return ' '.join(numbers_map[numbers_list])

# Unit tests
numbers_input = "three one five"
numbers_map = {
    "zero": "",
    "one": "one",
    "two": "two",
    "three": "three",
    "four": "four",
    "five": "five",
    "six": "six",
    "seven": "seven",
    "eight": "eight",
    "nine": "nine"
}

def test_sort_numbers():
    actual_result = sort_numbers(numbers_input)
    assert actual_result == "one two three four five"  # Expected result

test_sort_numbers()
``` 
This code defines a Python function `sort_numbers` that takes a space-separated string of numbers and returns the sorted string. The `numbers_map` dictionary is used to map each number to its sorted string. The `test_sort_numbers` function is the test case for the `sort_numbers` function, which checks that the function's output matches the expected result for the input string. 
This code demonstrates a way to solve the problem of sorting numbers in Markdown code.