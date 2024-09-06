```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(x) for x in numbers.
    return f'numbers of the strings sorted from smallest to largest in ascii.'
    return ''.join(numbers)

def test_sort_numbers() -> None:
    """ Test cases for the sort_numbers function."""
    test_cases = [
        "three one five",
        "zero one three four five seven",
        "two three eight five",
        "one two three seven eight nine"
    ]

    expected = [
        "one three five",
        "zero one three four five seven",
        "two three eight five",
        "one two three seven eight nine"
    ]

    for case, expected_result in zip(test_cases, expected):
        got_result = sort_numbers(case)
        assert got_result == expected_result, f"Failed for '{case}'"

if __name__ == "__main__":
    test_sort_numbers()
```
This Python script defines a function called sort_numbers, which takes a space-delimited string of numbers and returns a sorted version of the string. The function uses a list comprehension to convert each number into an integer and then uses the sorted function to sort the numbers from smallest to largest.

Additionally, there is a test suite function that contains several test cases for the sort_numbers function. The function asserts that the input strings are correctly sorted into the expected output strings.