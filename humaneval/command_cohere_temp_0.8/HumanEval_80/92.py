```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s[0:3])
    if len(letters_set) < 3:
        return False
    for i in range(3, len(s)):
        if s[i] in letters_set:
            return False
    return True
```

The following tests correspond to the problem statement:
```python
# test happy strings
test_strings = ['abcd', 'adb', 'xyu', 'lew']
for s in test_strings:
    assert is_happy(s) == True

# test unhappy strings
test_strings = ['aab', 'aaa', 'sid', 'foo']
for s in test_strings:
    assert is_happy(s) == False
```

This code defines the `is_happy` function. It works by first checking if the given string has a length of at least 3. If not, it returns `False` immediately. Then, it checks if the first three letters of the string make a unique set, if not, it returns `False`. It loops through the rest of the string incrementally checking that the 4th, 7th, 10th letters and so on are distinct. Finally, if none of these conditions are true, it returns `True`.  The corresponding tests assert the behavior of the function against happy and unhappy strings as described in the problem statement.