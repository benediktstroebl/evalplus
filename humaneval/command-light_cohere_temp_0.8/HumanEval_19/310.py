Here is a self-contained Python script that defines a function sort_numbers that sorts a list of numbers in a markdown code block:
```python
import unittest
from typing import List


def sort_numbers(numbers: List[int]) -> List[str]:
    """ Input is a list of numbers from zero to nine.
    Return a string with numbers sorted from smallest to largest.
    >>> sorted(range(0,10))
    ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    """
    return ' '.join(str(x) for x in numbers)


class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers():
        """Test the sort_numbers function"""
        numbers = [3, 1, 5]
        expected = ['one', 'three', 'five']
        got = sort_numbers(numbers)
        unittest.assert assert expected == got
        expected

    def test_sort_numbers_error():
        """Test the sort_numbers function with invalid input"""
        numbers = 'three one five'
        with unittest.assertRaises(TypeError):
            sort_numbers(numbers)

if __name__ == '__main__':
    unittest.main()
```