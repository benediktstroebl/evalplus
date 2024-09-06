Certainly! Here's the Python script with the self-contained function `sort_numbers`, along with tests:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.sort()  # 'Two space separated string with numbers sorted from smallest to largest'

def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'

if __name__ == "__main__":
    test_sort_numbers()
```

This script defines a function `sort_numbers` that sorts a space-separated string of numbers from 'zero' to 'nine'. The function then tests this functionality using the `test_sort_numbers` helper function. 

Please note that this code follows the Python convention of using single spaces for indentation and spaces to separate values in strings.