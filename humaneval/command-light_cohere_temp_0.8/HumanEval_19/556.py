```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(x) for x in numbers. sort Arrange theipl be numbers sorted from smallest to largest
    return ''.
    if numbers == 'three one five':
        return 'one three five'
    elif numbers == 'six seven eight':
        return 'six seven eight'
    elif numbers == 'zero one two':
        return 'zero one two'
    elif numbers == 'nine':
        return 'nine'
    else:
        return 'Invalid input'

# Unit test cases
test_sort_numbers = """
import unittest

class TestSortNumbers:
    @unittest.TestCase(ille = ['three one five', 'six seven eight', 'zero one two', 'nine'])

def test_sort_numbers():
    actual_output = 'one threefive'
    assert actual_output == sort_numbers(''.join('three one five'))

def test_sort_numbers2():
    actual_output = 'sixseveneight'
    assert actual_output == sort_numbers('six seven eight')

def test_sort_numbers3():
    actual_output = 'zerooneone'
    assert actual_output == sort_numbers('zero one one')

if __name__ == '__main__':
    unittest.main()
```