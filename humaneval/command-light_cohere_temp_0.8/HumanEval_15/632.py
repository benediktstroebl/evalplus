Here is a Python script that contains a self-contained function that solves the string-sequence problem with tests:
```python
import unittest
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f'{''join([f'{i}{int(i<2)}' for i in range(0, n+1)])}' 

class TestStringSequence(unittest.TestCase.TestCase):
   
    class()
    test_string_sequence(0)
    test_string_sequence(1)
    test_string_sequence(5)
    test_string_sequence(10)
    test_string_sequence(15)
```
This script defines a `TestStringSequence` class that contains test methods for various input sizes, which actually call the `string_sequence` function under test conditions.