Here's the self-contained Python script that defines a function sort_numbers that solves the problem of sorting numbers in Markdown code block: 

```python
# we are solving sorting numbers in ascending order using Python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split().apply(lambda x: x if x.isdigit() else 0,9 else x)
                    return x.sort()

    return ''.join_string(sorted(numbers))

# Unit tests
def test_sort_numbers():
    numbers = "three one five"
    expected = "one three five"
    result = sort_numbers(numbers)
    assert result == expected

# Run the tests
test_sort_numbers()
```