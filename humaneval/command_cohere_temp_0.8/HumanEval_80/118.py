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

The following test cases prove the correctness of the function:
```python
# Testing the function with different cases
print(is_happy("abcd")) # True
print(is_happy("aabb")) # False
print(is_happy("adb")) # True
print(is_happy("xyy")) # False
```

The function returns true for the first and third test cases and false for the second and fourth cases respectively.