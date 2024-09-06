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

This code defines a function `is_happy` that takes a string `s` as input and checks whether it is happy as defined in the problem statement. It first checks if the length of the string is at least 3, if not, it returns False. Then, it checks if the consecutive letters within a window of 3 are distinct, if they are not, it returns False, otherwise, it returns True. 

You can test this function using assert statements like so:
```python
assert is_happy("abcd")
assert is_happy("adb")
assert !is_happy("aabb")
assert !is_happy("xyy")
assert !is_happy("aa")
```

This will verify the correctness of the solution and ensure that it aligns with the given problem statement.