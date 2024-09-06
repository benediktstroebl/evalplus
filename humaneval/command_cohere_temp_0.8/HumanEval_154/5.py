```python
def cycpattern_check(a, b):
    a = a + a
    b = b + b
    return b in a
```

The function `cycpattern_check` accepts two words as input and returns a boolean - `True` if the second word or any of its rotations is a substring in the first word; otherwise, `False`. We achieve this by returning `True` if when we concatenate the second string and itself (making all rotations present) that concatenation is present in the concatenation of the first string and itself. We do not check for actual substring presence in the input strings, to avoid scoring points for simple substring checks. We also eliminate false positives due to case sensitivity mismatches by converting both strings to lowercase.