```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels
    vowels = set(['A', 'E', 'I', 'O', 'U'])
    # Initialize the counter
    count = 0
    # Iterate through the string
    for i in range(0, len(s), 2):
        if s[i] in vowels and s[i].isupper():
            count += 1
    return count
```

This Python script defines a function `count_upper()` which takes a string as an argument and counts the number of uppercase vowels in even indices of the string. The `vowels` set stores all the uppercase vowels that will be used in the iteration. The script then loops through the string at intervals of 2 indices using the `range()` function. It checks if the character at that index is an uppercase vowel using the `isupper()` method and if it is in the `vowels` set, it increments the count. Finally, the function returns the total count of uppercase vowels in even indices of the string.