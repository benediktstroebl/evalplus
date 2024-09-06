```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_occurrence = {}
    for i in range(len(s)-2):
        first_letter = s[i]
        second_letter = s[i + 1]
        third_letter = s[i + 2]
        if (first_letter, second_letter, third_letter) in letters_occurrence:
            return False
        letters_occurrence[(first_letter, second_letter, third_letter)] = True
    return True
```

The script uses an empty dictionary `letters_occurrence` to keep track of the occurrences of every 3 consecutive letters appearing in the string. The function checks if the dictionary contains a key with the current 3 consecutive letters before returning `False` if the answer isn't happy. It also returns `False` if the string length is less than 3. The script returns `True` if the answer is happy. 

This solution can be improved by using more efficient data structures like sorting and linearly checking the unvisited occurrences, but it still works and complies with the problem statement.