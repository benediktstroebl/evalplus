```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(letters_set) >= 3 and s[i] in letters_set:
            return False
        letters_set.add(s[i])
    return True
```

The function uses a set data structure to store the letters of the string. It loops through the string with a window of size 3 and checks if the set has more than or equal to 3 elements and all of them are present in the window. If this is the case for any window then the function returns False. Otherwise, it returns True. The overall time complexity of this solution is O(n) where n is the length of the string.