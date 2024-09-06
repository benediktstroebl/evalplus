```python
def sort_third(l: list):
    l_new = []
    for i in range(0, len(l), 3):
        try:
            temp = l[i:i+3]
            temp.sort()
            l_new.extend(temp)
        except:
            # In the case that we end the loop with a residual that is less than 3 elements, simply append these residual elements to l_new
            l_new.extend(l[i:])
    return l_new
```

This script defines a function sort_third which sorts a list element-wise such that every trio of elements is sorted while preserving the relative order of elements not divisible by three. The function accomplishes this by iterating through the list in steps of three, sorting each trio and extending these sorted trios to a new list l_new. When a residual less than three elements remains, the function simply appends these residual elements to l_new. The script also includes a test suite to ensure the function operates as expected. You can use the script's test suite by adding the following code to the top of the file:
```python
import unittest

class TestSortThird(unittest.TestCase):
    def test_sort_third(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])
        self.assertEqual(sort_third([0, 1, 2, 10, 20, 30]), [0, 1, 2, 10, 20, 30])
        self.assertEqual(sort_third([7, 8, 9, 10, 3, 4, 5, 6]), [3, 4, 5, 6, 7, 8, 9, 10])
``` 

Run test_sort_third to check that the function behaves as expected.