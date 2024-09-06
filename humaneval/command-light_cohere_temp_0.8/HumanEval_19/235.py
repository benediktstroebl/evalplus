```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split(" ").sort(numbers.split(' ', reverse=True)  ['0123456789'])
    return ''.join_strings(numbers)
    pass

# Test cases
test_sort_numbers = []
test_sort_numbers.append(['zero', 'two', 'one', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
test_sort_numbers.append(['ten', 'twelve', 'eleven'])
test_sort_numbers.append(['a', 'b', 'c'])

# Assertions
for test in test_sort_numbers:
    actual = sort_numbers(test)
    assert actual == ''.join_strings(test)

print("All tests passed!")
```