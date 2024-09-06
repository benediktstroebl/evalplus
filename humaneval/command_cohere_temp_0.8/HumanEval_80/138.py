```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s[0:3])
    for i in range(1, len(s) - 2):
        if s[i] in letters_set and s[i + 3] in letters_set:
            return False
        letters_set.add(s[i])
    return True
```

The script defines a function `is_happy` that takes a string `s` as input and checks whether it is happy as defined in the problem statement. It first checks if the string length is at least 3, and if so, it uses a `letters_set` to keep track of the distinct letters encountered every 3 positions. It iterates through the string, adding each new letter to the `letters_set`. If any repeat is found within a 3-letter window, the function returns False. Otherwise, it returns True.