```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This Python script defines a function `unique_digits` that takes a list of positive integers as input (`xs`). It filters this list using a list comprehension to include only those integers whose digits are all odd, and then sorts this filtered list in ascending order. The conditional statement `not any(int(y) % 2 == 0 for y in str(x))` checks whether any digit of the current integer is even, using a generator expression to iterate over all digits in the string representation of the integer `x`. The function then returns this sorted list.

The best practice for testing this function would be to include a suite of tests covering different scenarios in the `__main__` block and assert the expected outputs against the actual outputs for each case. Here, only the simplest case is tested to keep the snippet compact. You may want to add more tests depending on the complexity of your data and specific requirements:
```python
def test_unique_digits():
    # Test case from the docstring
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

    # Test case with no elements satisfying the condition
    assert unique_digits([152, 323, 1422, 10]) == []

    # Test case with only elements satisfying the condition
    assert unique_digits([1, 15, 33, 321]) == [1, 15, 33, 321]

``` 
If you are using Python 3.8 or later, you can use the `match` assertion introduced in the `unittest` framework, which allows more expressive and readable test assertions:
```python
from unittest.mock import patch
from unittest import TestCase

class TestUniqueDigits(TestCase):
    @patch('builtins.input', side_effect=['15,33,1422,1', '152,323,1422,10', '1,15,33,321'])
    def test_unique_digits(self, mck):
        expected = [1, 15, 33, 321]
        for input_ in ['15,33,1422,1', '152,323,1422,10', '1,15,33,321']:
            actual = unique_digits(input_.split(','))
            self.assertEqual(actual, expected)
``` 
In this version, each test case is defined using the `@patch` decorator and the `side_effect` parameter to simulate the list of strings as inputs, which allows us to avoid repeating the test cases in different assertions. The `test_unique_digits` method iterates through each input, calling the function with the input split by commas, and checks if the actual output matches the expected output using the `self.assertEqual` method.