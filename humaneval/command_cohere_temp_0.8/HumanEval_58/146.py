```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes in two lists, `l1` and `l2` as arguments. It uses the `set` function to remove duplicate elements and inherits the ordering of the set from the sorted input in `l1` and `l2`. The `intersection` method returns a set of the common elements between the two lists, which are then returned.

This solution is efficient and requires no additional libraries. Here is an example of how you can test the function using the doctest module:
```python
import unittest

def common(l1, l2):
    return sorted(set(l1).intersection(l2))

class TestCommon(unittest.TestCase):
    def test_result(self):
        """Test if the result is correct."""
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])

    def test_common(self):
        """Test if common elements are returned."""
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

    def test_unique(self):
        """Test if only unique common elements are returned."""
        self.assertEqual(common([10, 20, 30, 40], [30, 40, 50, 60]), [30, 40])

if __name__ == '__main__':
    unittest.main()
```

This will run the `unittest` framework, which will run the three individual test methods to ensure that the `common` function is working as expected.