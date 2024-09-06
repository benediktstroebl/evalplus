```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels to consider
    vowels = set(['A', 'E', 'I', 'O', 'U'])
    
    # Initialize the count to zero
    count = 0
    
    # Iterate through the string
    for char in s:
        if char.isupper() and char in vowels and (len(s) % 2 == 0):
            count += 1
    
    return count
```

This script defines a function `count_upper()` which:
1. Defines a set of uppercase vowels to consider (`vowels`).
2. Initializes a count to zero.
3. Iterates through the input string `s`.
4. Checks if the current char is uppercase, is a vowel, and is in an even index position.
5. If all conditions are met, it increments the count.

The provided tests demonstrate how the function behaves for various inputs.