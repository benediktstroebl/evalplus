```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(set([s[i], s[i+1], s[i+2]])) != 3:
            return False
    return True
```

The following tests evaluate the correctness of the function:
```python
# Test if a non-happy string is correctly identified
test_cases = ['a', 'aa', 'abcd', 'aabb', 'adb', 'xyy']
expected_results = [False, False, True, False, True, False]
for i in range(len(test_cases)):
    assert is_happy(test_cases[i]) == expected_results[i]
```

The test cases cover a wide range of scenarios, including edge cases, and the expected results are correctly predicted by the function. Feel free to modify the test cases or ask for additional assistance to satisfy any specific requirements or further evaluate the function.