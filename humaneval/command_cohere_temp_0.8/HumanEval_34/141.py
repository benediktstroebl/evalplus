```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This approach utilizes a set, `seen`, to keep track of unique elements encountered while iterating through the list `l`. Elements not in the set are added to the result list, which is then sorted. This guarantees a sorted list of unique elements. 

To pass tests, you can define a test list and compare the expected outcome with the result of the unique function when applied to that test list. Here's an example of how you can test this function:
```python
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = unique(test_list)
print(test_result)  # Output: [0, 2, 3, 5, 9, 123]
``` 

This would return the expected outcome for the test case provided in the problem statement. 
Make sure to have an appropriate testing framework like `pytest` or `unittest` to write more comprehensive tests for various scenarios and edge cases. 
If you want to use `unittest`, you can incorporate it into your script with:
```python
import unittest

class TestUnique(unittest.TestCase):
    def test_unique(self):
        self.assertEqual(unique(test_list), [0, 2, 3, 5, 9, 123])
``` 

Here `TestUnique` is a custom test class that inherits from `unittest.TestCase`, and `test_unique` is a test method that verifies if the `unique` function's output matches the expected outcome for the given `test_list`. 

This structured approach to testing will help ensure the correctness of your function for various cases, safeguarding against potential bugs in the future.