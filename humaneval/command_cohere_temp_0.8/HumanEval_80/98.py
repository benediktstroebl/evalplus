```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0, 0, 0]
    for letter in s:
        letters_count[letter] += 1
    return all(count % 3 == 0 and count > 0 for count in letters_count)
```

The function `is_happy()` takes a string as an input and first checks if the length of the string is at least 3, so it returns False immediately if it's shorter than that. Then it uses a list `letters_count` to count the occurrences of the last 3 letters in the string, if any of these counts isn't a multiple of 3 or is less than 3, the loop will identify it and the function will return False. Otherwise, it returns True.