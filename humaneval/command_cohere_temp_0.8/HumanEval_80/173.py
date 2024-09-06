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

This Python script defines a function called `is_happy` that takes a single argument - a string `s`. This function returns True if the string is happy, meaning its length is at least 3 and every set of 3 consecutive letters are distinct, otherwise it returns False. This behavior is defined by the following logic:
```
1.  If the length of the string is less than 3, it is not happy, so the function returns False.
2.  The function initializes a set called `letters_set` to store unique letters from the string.
3.  It loops through the string, starting from the first index, and checks if the set's size is equal to or greater than 3. If it is, and the current letter is already in the set, it means that not every set of 3 consecutive letters are distinct, so the function returns False.
4.  Otherwise, the function adds the current letter to the set and continues to the next letter in the string.
5.  If the loop completes without encountering any violations, the string is happy, so the function returns True.
```

This solution employs set theory to efficiently check for happyness in a string, optimizing performance and maintaining a concise code structure.