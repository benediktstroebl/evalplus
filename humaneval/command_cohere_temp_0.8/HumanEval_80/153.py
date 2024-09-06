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

This code defines a function `is_happy` that takes a string `s` as input and checks whether it is happy as defined in the problem statement. It first checks if the string's length is at least 3, and if not, it returns `False`. Then, it iterates through the string subtracting consecutive letters sets of 3 to check if they are all unique. If the condition is not met for any of the trips, it returns `False`. If the loop completes, the function returns `True`. 

This solution works accordingly for the provided test cases and should be fully self-contained within the designated markdown code block. 
```python
# Test Cases
assert is_happy("abcd")
assert not is_happy("aabb")
assert is_happy("adb")
assert not is_happy("xyy")
assert not is_happy("aaa")
```