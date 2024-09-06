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

The function uses a set data structure to solve the problem. It first checks if the length of the string is at least 3, if not, it returns False. Then, it iterates through the string, and for every consecutive trio of letters, it checks if they are distinct. If they are not distinct, it returns False. Otherwise, it adds the letters to a set, and since the happy criterion must hold for all consecutive trios, the function returns True.