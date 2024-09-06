```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine. Valid choices are options are zero, one, two, three, four, five, six, seven, eight and nine."""
    # Separate numbers and alphabet
    numbers = numbers.split()
    strings = [num.split('.') for num in numbers]

    # Sort strings
    sorted_strings = sorted(strings)

    # Join strings with spaces
    result = ' '.join(sorted_strings)

    return result

# Unit tests
def test_sort_numbers():
    test_str = "three one five"
    expected = "one three five"
    result = sort_numbers(test_str)
    assert result == expected, f"Result is {result}, expected {expected}"

if __name__ == "__main__":
    test_sort_numbers()
```
This Python script defines a function `sort_numbers` that takes a string of numbers and returns a sorted version of the numbers. The function splits the strings into a list of numbers and then sorts the numbers while also ensuring that strings are correctly formatted. The script also has a unit test using the `test_sort_numbers` function to ensure that the `sort_numbers` function produces the correct results.