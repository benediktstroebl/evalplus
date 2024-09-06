```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([x for x in txt if x.isalpha() and x.lower() not in 'abcdefghijklmnopqrstuvwxyz'])
    return ans
```
```python
import unittest
class TestSplitWords(unittest.TestCase):
    def test_split_words(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
    def test_split_words2(self):
        self.assertEqual(split_words("Hello, world!"), ["Hello", "world!"])
    def test_split_words3(self):
        self.assertEqual(split_words("abcdef"), 3)
if __name__ == '__main__':
    unittest.main()
```