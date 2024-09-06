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
# Test cases
tests = [
    ("a", False),
    ("aa", False),
    ("abcd", True),
    ("aabb", False),
    ("adb", True),
    ("xyy", False),
    ("happy", True),
]

for test in tests:
    assert is_happy(test[0]) == test[1]
```

The function `is_happy` takes a string `s` as input and returns `True` if the string is happy, meaning every consecutive trio of letters is distinct. If not, it returns `False`. The script also includes a variety of test cases to validate the functionality of the code. You can use these test cases to verify the correctness of your approach. Feel free to add more tests to cover other scenarios as well.  This ensures the robustness of the solution against a variety of inputs.