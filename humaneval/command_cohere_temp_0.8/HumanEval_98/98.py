```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Ensure the string contains at least one character
    if not s:
        return 0
    
    # Declare variable to store the result
    count = 0
    
    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Check if the character is an uppercase vowel
        if char.isupper() and char in 'AEIOU':
            # Check if the index is even
            if i % 2 == 0:
                count += 1
    
    # Return the final count
    return count
```

The script adheres to the problem's specifications, defining a function `count_upper` that accepts a string `s` and returns the number of uppercase vowels in even indices. The `enumerate` function is used for each character's indexing, and the `isupper` and `in` functions are used for character validation. The result is accumulated in the `count` variable, which is returned upon completion. The total time complexity of the script is O(N), where N represents the string's length.