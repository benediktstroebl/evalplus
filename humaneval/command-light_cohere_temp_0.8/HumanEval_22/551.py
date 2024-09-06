```python
from typing import List

def filter_integers(values):
    return [i for i in values if type(i) == int]

# Test case 1
values_test1 = ['a', 3.14, 5]
result_test1 = filter_integers(values_test1)
assert result_test1 == [5], "Test case 1 failed."

# Test case 2
values_test2 = [1, 2, 3, 'abc', {}, [0]]
result_test2 = filter_integers(values_test2)
assert result_test2 == [1, 2, 3], "Test case 2 failed."
```
This Python code defines a function called `filter_integers` that takes a list of values as an argument and returns a new list containing only the integers from the input. The function uses a list comprehension and the `type()` function to filter out non-integer values from the input list. The code also includes two test cases:

1. Test case 1: In this test, the function is called with the list `values_test1`, which contains various types of values, including strings, floating-point numbers, and integers. The expected output is `[5]` (an integer), which is the only integer in the input list.

2. Test case 2: This function is called with the list `values_test2`, which contains a mix of data types, including integers, strings, and other objects. The expected output is `[1, 2, 3]` (the integers in the input list).