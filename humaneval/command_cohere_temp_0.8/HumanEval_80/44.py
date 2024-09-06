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

This code defines a function `is_happy` that takes a string `s` as input and checks whether it is happy as described in the prompt. It works by first checking if the length of the string is at least 3. If not, it returns False immediately, as such a string cannot be happy. Otherwise, it uses a set `letters_set` to keep track of the letters encountered. It iterates through the string skipping the first and last characters, and checks if every group of 3 consecutive letters are distinct. If they are not, or if after the iteration any 3 letters are found in the set, it returns False. Otherwise, it returns True.