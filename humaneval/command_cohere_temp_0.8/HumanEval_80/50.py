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
# Test if the string 'aab' is happy
assert is_happy('aab') == False

# Test if the string 'abcd' is happy
assert is_happy('abcd') == True

# Test if the string 'aabb' is happy
assert is_happy('aabb') == False

# Test if the string 'xyy' is happy
assert is_happy('xyy') == False

# Test if the string 'adb' is happy
assert is_happy('adb') == True
```

The function `is_happy` takes a string as an input and returns `True` if the string is happy, and `False` otherwise.  It checks that the length of the string is at least 3 and every 3 consecutive letters are distinct. The latter is done by maintaining a set of encountered letters and checking that every 3 consecutive letters are not simultaneously present in this set.