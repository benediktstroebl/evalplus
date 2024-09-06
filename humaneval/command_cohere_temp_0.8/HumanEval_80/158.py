```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(letters_set) >= 3 and s[i] in letters_set:
            return False
        letters_set.add(s[i])
    return True
```

The following tests are contained within the script:
```python
def test_is_happy():
    assert is_happy("abcd")
    assert not is_happy("aabb")
    assert is_happy("adb")
    assert not is_happy("xyy")
    assert not is_happy("aaa")
    assert is_happy("abcbcbb")

test_is_happy()
```

When the script is executed, the `test_is_happy()` function will run the specified tests, and the output will indicate whether the function's predictions correspond to reality.  Any of the following results will indicate true success:
- If the tests pass, the result will be something like `OK`
- If any test fails, the result will contain the name of the test that caused the failure, like `adb -> False`.
- If any exception happens during the running of a test, the exception name and the error will be in the result. For example, `TypeError: 'set' object does not support item assignment`.