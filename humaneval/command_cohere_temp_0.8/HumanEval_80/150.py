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

This code defines a function `is_happy` that takes a string `s` as input and checks whether it is happy as described in the prompt. It works by first checking if the length of the string is at least 3. If not, it returns False immediately, as such a string cannot be happy. Otherwise, it uses a set `letters_set` to keep track of the letters encountered in the string. Then, it iterates through the string, checking if every consecutive trio of letters is distinct. If it encounters a trio that is not distinct, it returns False. Otherwise, it returns True at the end. The code includes explicit returns after each check to ensure it terminates efficiently.