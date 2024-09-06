```python
from typing import List
def sort_numbers(input_string: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'. Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Returns the string with numbers sorted from smallest to largest.
    """
    split_str_string= input_string.split()
    delim_string= [int(num) for num in split_str]
    return ' '.join(sorted(del_str))

test_strings = [
    "three one five",
    "zero three seven",
    "one two three four",
    "two six eight nine"
]

for test_str in test_strings:
    actual_str = sort_numbers(test_str)
    assert actual_str == ' '.join(sorted(test_str.split())))
```