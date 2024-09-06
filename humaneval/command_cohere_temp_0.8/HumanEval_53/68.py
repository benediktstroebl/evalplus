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

The code provides a self-contained Python script with a function `add` that adds two numbers and a corresponding set of tests using the `unittest` module. When the script is run, the tests are automatically executed, ensuring that the function behavior matches the specifications provided. Thus, the code demonstrates a simple approach to testing functionalities and ensures the function works as expected. 
The function definition is:
```python
def add(x: int, y: int):
    return x + y
```

And the test case is:
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