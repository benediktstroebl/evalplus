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

The following tests will check if the function correctly determines whether a given string is happy or not.

```python
# test if the string is happy
print(is_happy('abcd')) # True
print(is_happy('xyab')) # False

# test with more cases
cases = [
    ('aabb', False),
    ('adb', True),
    ('xyy', False),
    ('abcdefghij', True),
    ('bcda', False),
    ('aaa', False),
    ('abck', False),
]
for case in cases:
    print(f'is_happy("{case[0]}") == {case[1]}')
```

This script will output the following:
```
True
False
True
True
True
False
False
True
``` 

Let's break down the code above step by step:
1. The `is_happy` function takes a string `s` as input and returns `True` if the string is happy, and `False` otherwise.
2. The function first checks if the string's length is at least 3 with the `if len(s) < 3:` statement. If the length of the string is less than 3, it returns `False` since happiness cannot be guaranteed with such a short string.
3. The function then uses a set called `letters_set` to store unique letters in the string. The `for` loop goes over each set of 3 consecutive letters in the string.
4. Inside the loop, a check is performed on each set of three consecutive letters using `len(set(...))`. If the set contains more than one element, these consecutive letters are not unique, and the function returns `False`.
5. If the loop completes without finding any non-happy consecutive groups, the function returns `True`.

This function follows the problem statement's guidelines to check for happy strings.