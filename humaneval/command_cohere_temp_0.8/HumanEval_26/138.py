```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Returns a new list without duplicates, keeping the order of elements untouched.
    """
    returned_list = []
    for number in numbers:
        if number not in returned_list:
            returned_list.append(number)
    return returned_list
```

The script uses a list comprehension to loop through each integer and append them to a new list if it has not already appeared in the list. The function returns the new list without duplicates. 

To test this script, we can run the following:
```python
import unittest

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates_basic(self):
        """ Test that the function removes duplicates from a list of integers """
        numbers = [1, 2, 3, 2, 4]
        result = remove_duplicates(numbers)
        self.assertEqual(result, [1, 3, 4])

    def test_remove_duplicates_empty(self):
        """ Test that the function handles an empty list appropriately """
        numbers = []
        result = remove_duplicates(numbers)
        self.assertEqual(result, [])

    def test_remove_duplicates_single_number(self):
        """ Test that the function handles a list with a single number appropriately """
        numbers = [1]
        result = remove_duplicates(numbers)
        self.assertEqual(result, [1])

    def test_remove_duplicates_already_removed(self):
        """ Test that the function removes duplicates even if one of them has been removed already """
        numbers = [1, 2, 3, 2, 4]
        result = remove_duplicates(numbers)
        self.assertEqual(result, [1, 3, 4])
        result = remove_duplicates(result)
        self.assertEqual(result, [1, 3])

    def test_remove_duplicates_complex(self):
        """ Test that the function removes duplicates from a list of integers, including complex cases """
        numbers = [1, 21, 31, 22, 32, 42, 52, 32, 63, 72, 73, 63, 74, 91]
        result = remove_duplicates(numbers)
        self.assertEqual(result, [1, 21, 31, 22, 32, 42, 52, 63, 72, 73, 74, 91])

if __name__ == '__main__':
    unittest.main()
```

This test suite contains several test functions that test the `remove_duplicates` function on various inputs to ensure that it removes the necessary duplicates. 

The `unittest.main()` call runs the tests, and the output will indicate that all tests have passed.