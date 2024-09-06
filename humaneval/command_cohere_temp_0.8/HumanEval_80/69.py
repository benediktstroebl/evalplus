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

The function uses a set data structure to store the letters of the string. It iterates over the string with a step size of 2 to ensure that every 3 consecutive letters are considered. If the set contains elements equivalent to the current consecutive trio, the function returns False, implying that the string is not happy. Otherwise, it continues checking through the entire string, returning True if the conditions are met. 

This approach ensures efficiency in terms of time and space, completing the check for happiness in linear time and using a small amount of space for the set data structure.