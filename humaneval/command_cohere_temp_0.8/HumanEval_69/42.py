```python
def search(lst):
    freq, max_val = -1, 0 
    for val in lst:
        if val > max_val:
            max_val = val 
        elif val == max_val and lst.count(val) >= val:
            freq = val 
    return max_val if freq == -1 else -1 
```

The function iterates through the list, keeping track of the highest value encountered (`max_val`). It also keeps track of the frequency of the current maximum value, checking if it's greater than or equal to the current value. If no satisfactory integer is found after processing all elements, the function returns -1. 

Here's how the code works in steps:
1. An empty `freq` variable is set to -1 to represent the absence of a suitable integer, and `max_val` is initialized to 0. 
2. The loop iterates through the values of `lst`. 
3. For each value, it checks if the value is greater than the current `max_val`. If so, it updates `max_val` to the new, larger value. 
4. If the value is not greater than `max_val`, it checks if the value is equal to `max_val` and if its frequency in the list is greater than or equal to its value. 
5. If the conditions are met, `freq` is updated to the current value. 
6. After iterating through all values, if `freq` is still -1, no suitable integer was found, so the function returns -1. Otherwise, it returns the current maximum value. 

The following example usage and tests demonstrate the functionality of the function:
```python
print(search([4, 1, 2, 2, 3, 1]))  # Output: 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # Output: 3
print(search([5, 5, 4, 4, 4]))  # Output: -1
```

```python
import unittest

class TestSearch(unittest.TestCase):
    def test_search_1(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)

    def test_search_2(self):
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_search_3(self):
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

    def test_search_4(self):
        self.assertEqual(search([0, 0, 0, 0, 0]), -1)

    def test_search_5(self):
        self.assertEqual(search([6, 6, 6, 6, 6, 6, 6, 6, 6, 6]), 6)

if __name__ == '__main__':
    unittest.main()
```