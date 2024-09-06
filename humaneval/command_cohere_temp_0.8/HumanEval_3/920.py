```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```

This script defines a function `below_zero` that takes in a list of `List[int]` and calculates the ending balance after each operation. If the balance goes negative at any point, the function returns `True`. Otherwise, it returns `False`. The script passes the given tests of returning `False` for the first test of `([1, 2, 3])` and returning `True` for the second test of `([1, 2, -4, 5])`. 
To test this script, you can run the following tests:
```python
TestBelowZero:
    def test_below_zero_true(self):
        self.assertTrue(below_zero([1, 2, -4, 5]))

    def test_below_zero_false(self):
        self.assertFalse(below_zero([1, 2, 3]))
```
Each test checks the function's output against the expected `True` or `False` value. 
This way, you can ensure that the function behaves as expected and conforms to the problem statement. 
If you want to specify additional test cases, you can add them to the test suite to comprehensively evaluate the functionality of the `below_zero` function.  You can use the `assert` statement to check if the output of the function is correctly returning True or False.