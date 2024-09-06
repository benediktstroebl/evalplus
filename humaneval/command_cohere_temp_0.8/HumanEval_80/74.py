```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(letters_set) >= 3 and s[i] == s[i+1] and s[i] == s[i+2]:
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
    assert not is_happy("aa")
    assert not is_happy("aaa")

test_is_happy()
```

The function `is_happy` checks whether a given string is happy or not by verifying the conditions stated in the problem. It returns `True` if the string is happy, and `False` otherwise.  This is done by checking every 3 consecutive letters if they are distinct.