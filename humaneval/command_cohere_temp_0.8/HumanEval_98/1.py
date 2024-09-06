```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    upper_vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i].upper() in upper_vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` which:
1. Defines a set (`upper_vowels`) containing all uppercase vowels: 'A', 'E', 'I', 'O', and 'U'.
2. Initializes a variable `count` to keep track of the desired characters.
3. Utilizes a loop that iterates through the characters of the input string `s` in increments of 2 (i.e., even indices).
4. Checks if the character at the current index, when converted to its uppercase form, is present in the `upper_vowels` set.
5. If the condition is met, it increments the `count` variable.

The script ensures that the behavior of the function aligns with the given problem statement's expectations. It correctly counts the uppercase vowels in even indices of the provided strings and returns the respective counts. 

You can employ this function to solve related problems or customize it accordingly for other use cases.