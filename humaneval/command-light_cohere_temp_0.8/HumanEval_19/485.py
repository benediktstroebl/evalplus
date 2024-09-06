```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))
    """
    assert sort_numbers('three one five') == 'one three five', "Input does not match expected output"
    assert sort_numbers('zero zero two') == 'zero zero two', "Input does not match expected output"
    assert sort_numbers('eight seven six') == 'eight seven six', "Input does not match expected output"
    assert sort_numbers('four three six') == 'four three six', "Input does not match expected output"
    return 

```