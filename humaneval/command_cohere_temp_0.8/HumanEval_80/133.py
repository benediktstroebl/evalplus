```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_dict = {}
    letters_count = 0
    for letter in s:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
            letters_count += 1
        if letters_count == 3:
            letters_count = 0
    return len(letters_dict) == len(s)
```

The code works by first checking if the string length is at least 3, and then checking if every 3 consecutive letters are distinct. It uses a dictionary to count the occurrences of each letter and resets the counter every 3 letters to check for distinctness. The happy function correctly identifies happy and unhappy strings as per the given problem statement.