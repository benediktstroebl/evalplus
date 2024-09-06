```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    counter = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in 'AEIOU':
            counter += 1
    return counter
```

This script defines a function `count_upper()`, which examines each character of the input string `s` in iterates in intervals of 2 indices using a for loop. When a character is encountered, the function tests if it is an uppercase vowel ('AEIOU') and if its index is even. Whenever these conditions are fulfilled, the function adds to the counter. Finally, the function returns the final count of uppercase vowels in even positions. 

The total time complexity of this code is O(N), where N represents the length of the input string `s`, as it checks each character of the string only once and in general, string indexing and character checking in Python are constant time operations.