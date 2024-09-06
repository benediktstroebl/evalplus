```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_occurrences = {}
    for i in range(len(s)-2):
        first_letter = s[i]
        second_letter = s[i + 1]
        third_letter = s[i + 2]
        if (first_letter, second_letter, third_letter) in letters_occurrences:
            return False
        letters_occurrences[(first_letter, second_letter, third_letter)] = True
    return True
```

The code uses a dictionary to store the occurrences of every group of three consecutive letters in the string. If every group of three letters is distinct, the function returns `True`, otherwise, it returns `False`.