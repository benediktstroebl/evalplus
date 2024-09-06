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

The code defines a function `is_happy` that takes a string `s` as input and checks whether it is happy as defined in the problem statement. It first checks if the length of the string is at least 3; if not, it returns False, since a string of length less than 3 cannot be happy. Next, it uses a set called `letters_set` to store the letters encountered, initially empty. Then, it loops through the string `s` with a step size of 3 (skipping the last 2 characters in each iteration) and checks if every 3 consecutive letters are distinct. The distinctness is determined by checking if the set `letters_set` reaches a size of 3 or more and if the current letter is already in the set, which indicates a repeat of a previously encountered letter. If either of these conditions is true, it returns False. If the loop completes without encountering any repeated letters, it returns True, indicating that the string is happy. The script provides an elegant and efficient solution to check if a string is happy based on the given criteria.  This approach ensures that the time complexity is O(n), where n is the length of the input string, as it processes the string once and performs set operations with constant time complexity.