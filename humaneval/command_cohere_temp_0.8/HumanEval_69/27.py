```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The `search` function takes a list of integers `lst` as input and returns the greatest integer that meets the conditions described in the problem prompt.

This solution utilizes a dictionary `freq` to store the frequency of each integer in the list. It first iterates through the list and updates the frequency count for each integer. Then, it uses the max function to compare the frequency of each integer with itself and calculates the maximum value that meets the criteria. Finally, it checks the maximum value obtained; if it's less than 1, no valid integer exists, so it returns -1, otherwise returns the greatest integer meeting the criteria. 

The previous response includes a test suite to ensure the correctness of the `search` function. Feel free to execute this test suite by modifying the code as follows:
```python
import unittest

class TestSearch(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)
    def test_example2(self):
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)
    def test_example3(self):
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)
    def test_does_not_exist(self):
        self.assertEqual(search([1, 2, 3, 4, 5]), -1)
    def test_zero_exists(self):
        self.assertEqual(search([0, 0, 1, 2, 3, 4, 0, 0, 5]), 0)
    def test_multiple_occurrences(self):
        self.assertEqual(search([3, 3, 3, 7, 7, 7, 5, 5, 5, 4, 4, 4, 4]), 4)

if __name__ == '__main__':
    unittest.main()
```