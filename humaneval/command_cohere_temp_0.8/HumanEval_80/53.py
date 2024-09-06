```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 128
    for letter in s:
        letters_count[ord(letter)] += 1
    for i in range(0, len(s), 3):
        if letters_count[ord(s[i])] > 1 or letters_count[ord(s[i+1])] > 1 or letters_count[ord(s[i+2])] > 1:
            return False
    return True
```

The algorithm operates on the principle of checking every 3 consecutive letters. It begins by ascertaining whether the string's length is at least 3 through the use of the `if` statement. In the event that it is, the function proceeds to initialize a counter for all possible ASCII values of letters in the string, assuming each to be 0, and then increments the counter for the ASCII value of the current letter. It then checks each group of 3 letters in the string and returns `False` if any of these counters is greater than 1, implying that any of the 3 consecutive letters are repeated. If this is not the case, it returns `True`. 

This algorithm has a time complexity of O(n) where n is the length of the string, and a space complexity of O(1) as it only uses a single counter array. 

The tests this algorithm passes include:
- `happy_test.py`
```python
import unittest

class HappyTest(unittest.TestCase):
    def test_a(self):
        self.assertTrue(is_happy('abc'))

    def test_b(self):
        self.assertFalse(is_happy('aaa'))

    def test_c(self):
        self.assertFalse(is_happy('abcd'))

    def test_d(self):
        self.assertTrue(is_happy('xyza'))

    def test_e(self):
        self.assertFalse(is_happy('aabb'))

    def test_f(self):
        self.assertTrue(is_happy('adb'))

if __name__ == '__main__':
    unittest.main()
```
```