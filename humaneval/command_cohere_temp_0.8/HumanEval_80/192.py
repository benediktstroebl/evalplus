```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 256
    for letter in s:
        letters_count[ord(letter)] += 1
    letters_count[0] -= 1  # one of the letters should be counted twice
    return all(count % 3 == 0 and count != 0 for count in letters_count[1:])
```

The script uses a dictionary to keep track of the occurrence of each letter in the alphabet and checks whether the criteria are met. Would you like to know more about any of the concepts used in this code?