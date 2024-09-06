```python
from typing import List
def sort_numbers(input_str: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are string can be zero, one, two, three, four, five, six, seven, eight, or nine.
    """
    Numbers are sorted in ascending order.
    return ''.join(sorted(input_str))
    """
    # Test cases
    assert sort_numbers('zero') == '0', "Zero is not sorted as zero"
    assert sort_numbers('two three') == '23', " incorrect sorting"
    assert sort_numbers('five four three') == '354', " Incorrect sorting"
    assert sort_numbers('nine') == '9', " Nine is not sorted as nine"
    assert sort_numbers('one eight seven six') == '1766', " Incorrect sorting"
    assert sort_numbers(' Ten eleven twelve') == '121', " incorrect sorting"
    return sort_numbers(' Nine eight seven ')
```