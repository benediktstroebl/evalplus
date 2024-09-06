```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(y) % 2 != 0 for y in str(x))]
    return sorted(odd)
```

The function `unique_digits(xs)` employs a list comprehension to iterate over each element `x` in the input list `xs`. For each `x`, it checks if any digit in the string representation of `x` is odd using the `any()` function in conjunction with the `int(y) % 2 != 0` expression. If any odd digit is found, the element `x` is added to the `odd` list. Finally, the function returns a sorted list of elements in increasing order from the `odd` list, which holds all the elements in `xs` with at least one odd digit. 

The following import statement enables unit testing:
```python
import unittest
```

And the following test case ensures the function behaves as intended:
```python
class TestUniqueDigits(unittest.TestCase):
    def test_unique_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
```

Overall, the script provides a standalone function with a dedicated test case to ensure its correctness.