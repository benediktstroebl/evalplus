```python
def add(x: int, y: int):
    return x + y
```
```python
import unittest
class TestAddFunction(unittest.TestCase):
    def test_add_2_3(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_5_7(self):
        self.assertEqual(add(5, 7), 12)
if __name__ == '__main__':
    unittest.main()
```