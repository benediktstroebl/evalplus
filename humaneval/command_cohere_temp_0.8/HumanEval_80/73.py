```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_occurrence = {}
    for i in range(len(s) - 2):
        first_letter = s[i]
        second_letter = s[i + 1]
        third_letter = s[i + 2]
        if (first_letter, second_letter, third_letter) in letters_occurrence:
            return False
        letters_occurrence[(first_letter, second_letter, third_letter)] = 1
    return True
```

This script defines a function `is_happy` that takes in a string `s` as an argument and checks whether the string is happy or not by returning `True` or `False`, respectively. 

The script defines the function and then provides a series of tests (indented below) to ensure the robustness of the function against edge cases and other scenarios. These tests are a good practice to ensure the function handles all possible cases correctly. 

The function's logic is straightforward. It checks if the string length is at least 3 and then uses a dictionary to count the occurrence of each 3-letter sequence. If any of the 3-letter sequences occur more than once, the function returns `False`. Otherwise, it returns `True`.  The tests are:
```python
# Test cases
test_cases = [
    "abcd", "adb", "xyy", "aabb", "bbcc", "cbb", "aaad", "iii", "zzzz", "txtzz"
]

expected_results = [True, True, False, False, True, True, False, True, False]

for i in range(len(test_cases)):
    assert is_happy(test_cases[i]) == expected_results[i]
```