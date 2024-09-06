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

This code defines a function `is_happy` that takes a string `s` as input and checks whether it is happy as described in the problem. It first checks if the length of the string is at least 3, if not, it returns False. Then, it checks if every 3 consecutive letters are distinct, if they are not, it returns False. If the string meets the conditions, it returns True.  This solution has a time complexity of O(n) where n is the length of the input string `s`. 

You can test this function with the following strings to confirm it works as expected:
```python
print(is_happy('abcd'))  # True
print(is_happy('aabb'))  # False
print(is_happy('adb'))  # True
print(is_happy('xyy'))  # False
``` 

This version of the script is more efficient and safer, since it doesn't make assumptions regarding the input range or kind of letters, and it has a more efficient time complexity of O(n) compared to the previous version.