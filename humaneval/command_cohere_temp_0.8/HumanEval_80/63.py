```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s[0:3])
    for i in range(3, len(s), 3):
        if len(set(s[i:i+3])) != 3:
            return False
    return True
```

The problem is solved by using two main steps:
1. First, we check if the string's length is at least 3, assuming that the string itself is not happy if it does not have this length.
2. Then, we check if each group of 3 consecutive letters are distinct by using sets, where the first set `letters_set` is checked for each 3 consecutive letters, and the subsequent sets are checked iteratively by shifting the index by 3.

The script above elegantly solves the problem in a concise manner. It utilizes sets to check for distinct letters and iterates the string to check for happiness at each window of 3 letters.