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

This script defines a function `is_happy` that takes a string `s` as input and checks whether the string is happy or not. The function returns True if the string is happy, and False otherwise. 

The script assumes that the string's length is at least 3 to once write that every 3 consecutive letters are distinct. The script uses a set to store the letters to check the uniqueness of every 3 consecutive letters. It starts by checking the first 3 letters and continues further to check every 3 consecutive letters. If the set's size is less than equal to 3 and the current letter is already present in the set, then it is not distinct, and the function returns False. Otherwise, it adds the letters to the set and continues the process until the end of the string. If the complete iteration passes through, the script returns True as the solution.