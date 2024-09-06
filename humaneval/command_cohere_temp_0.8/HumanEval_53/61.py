```python
def add(x: int, y: int):
    return x + y
```
```python
>>> add(2, 3)
5
>>> add(5, 7)
12
```
```python
import unittest
class TestAddFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    def test_large_numbers(self):
        self.assertEqual(add(5, 7), 12)
if __name__ == '__main__':
    unittest.main()
```