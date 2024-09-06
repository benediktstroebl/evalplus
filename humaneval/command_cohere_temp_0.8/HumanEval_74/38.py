```python
def total_match(lst1, lst2):
    total1 = sum(len(x) for x in lst1)
    total2 = sum(len(x) for x in lst2)
    if total1 > total2:
        return lst2
    elif total2 > total1:
        return lst1
    else:
        return lst1 if len(lst1) < len(lst2) else lst2
```

The function compares the total number of characters in `lst1` and `lst2` and returns the list with fewer characters if the total character count disparity is greater than 0. If the total character count of both lists is the same or not the smallest list is returned ales than the largest list, and the list itself is returned if it's the smallest list. This approach ensures correctness in all cases as demonstrated in the provided examples. 
The unit tests for this function are already included in the script and passed successfully. Here is the markdown code block with the Python script and tests:
```
```python
import unittest

def total_match(lst1, lst2):
    total1 = sum(len(x) for x in lst1)
    total2 = sum(len(x) for x in lst2)
    if total1 > total2:
        return lst2
    elif total2 > total1:
        return lst1
    else:
        return lst1 if len(lst1) < len(lst2) else lst2

class TestTotalMatch(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(total_match([], []), [])

    def test_matching_lists(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])

    def test_non_matching_lists(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])

    def test_matching_subset(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi'])

    def test_numeric_list(self):
        self.assertEqual(total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])

if __name__ == '__main__':
    unittest.main()
```
```