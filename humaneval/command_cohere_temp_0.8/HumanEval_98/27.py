```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    c = 0
    for i, char in enumerate(s):
        if char.isupper() and char in 'AEIOU' and (i%2==0):
            c+=1
    return c
```
This script defines a function `count_upper()` which iterates through the string `s` and counts the number of uppercase vowels in even indices. The conditions for checking if a character is an uppercase vowel and if it's in an even index are all within the for loop. The script ensures that the function returns 0 for non-alphabetic strings and also passes the other test cases provided.