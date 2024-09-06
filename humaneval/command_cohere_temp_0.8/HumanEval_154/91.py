```python
def cycpattern_check(a, b):
    a = a + a
    b = b + b
    return b in a
```

The function `cycpattern_check` accepts two words as input and tests for the second word's substring in the first word. It also checks if any rotation of the second word is a substring in the first by extending the first word to double its length. It returns `True` if any rotation of the second word is a substring in the first word, and `False` otherwise. 

Here are some example inputs and expected outputs as test cases to ensure the function is working correctly:
```python
test_cases = [
    ("abcd", "abd", False),
    ("hello", "ell", True),
    ("whassup", "psus", False),
    ("abab", "baa", True),
    ("efef", "eeff", False),
    ("himenss", "simen", True)
]

for test_case in test_cases:
    assert cycpattern_check(*test_case) == test_case[2]
```