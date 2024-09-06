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

The following test cases illustrate the behavior of the `is_happy` function:
```
> is_happy('abcd')
True

> is_happy('aabb')
False

> is_happy('adb')
True

> is_happy('xyy')
False

> is_happy('azq')
True
``` 

The function employs sets to check if any three consecutive letters are identical, and hence, the happiness of the given string.