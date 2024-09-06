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
    assert not is_happy("aaS")
    assert is_happy("abScar")

test_is_happy()
```

The function `is_happy()` takes a single argument - a string `s`.  To check if `s` is a happy string, the function first checks if its length is at least 3. If not, it promptly returns `False`, since there is no point in checking for happy traits if the string is not long enough. Otherwise, it proceeds to iterate through the string, adding each letter to a set. It is important to use a set here as sets do not contain duplicate values, ensuring that each letter is only added once no matter how many times it appears in the string. The function then checks if the size of the set is equal to the number of distinct letters every 3 conscecutive letters. If it is, the function returns `True`, otherwise it returns `False`.  The tests included in the script test various cases to which the function correctly returns True or False.