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

This Python script defines a function called `is_happy` that takes a single string as an input. This function returns True if the string is "happy"—a string where the consecutive letters are distinct every 3 letters. Otherwise, it returns False. This function is self-contained and can be used to solve the specific problem described in the prompt.  The given implementation has a time complexity of O(n) where n is the length of the string and an auxiliary space complexity of O(1) as it doesn't require any additional memory except for the variable used for looping.