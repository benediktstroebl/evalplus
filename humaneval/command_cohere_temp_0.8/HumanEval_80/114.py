```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(set([s[i], s[i + 1], s[i + 2]])) != 3:
            return False
    return True
```

The following tests will check if the function correctly determines happy and unhappy paths:
```python
# Happy paths
test_cases = [
    ("abcd", True),
    ("adb", True),
    (" xy y", False),
    ("aaab", False),
    ("aabb", False),
    # Add more happy paths here
]

for string, expected in test_cases:
    assert is_happy(string) == expected, f"Expected {expected} but got {not expected}" for string, expected in test_cases

# Unhappy paths
test_cases = [
    ("aa", False),
    ("aaa", False),
    ("abbb", False),
    ("xyyx", False),
    ("xzcx", False),
    # Add more unhappy paths here
]

for string, expected in test_cases:
    assert is_happy(string) == expected, f"Expected {expected} but got {not expected}"
``` 

The function returns True if the string is happy, and False otherwise. 
Every three consecutive letters in the string are compared and stored in the `letters_set` using a set. The next three letters are checked for uniqueness by seeing if the length of `letters_set` is still 3 after adding them. The function returns False if any of these groups of three letters are not unique.  Otherwise, it returns True, indicating a happy path.  This solution has a time complexity of O(n) and is relatively efficient.  It can be enhanced further using memoization to avoid recomputation of consecutive letter sets.