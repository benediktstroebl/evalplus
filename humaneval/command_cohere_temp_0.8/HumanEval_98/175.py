Here's a Python script that contains a function named `count_upper()` which solves the problem as described in the prompt:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Use a dictionary to store the number of uppercase vowels in even indices encountered so far.
    vowel_count = {}
    # Iterate over each character in the string.
    for i, char in enumerate(s):
        # Check if the character is an uppercase vowel.
        if char.isupper() and char in 'AEIOU':
            # Check if the character is in an even index and update the count if so.
            if i % 2 == 0 and s[i] in vowel_count:
                vowel_count[s[i]] += 1
        # Check if we've reached the middle of the string and if so, return the count.
        if i == len(s) // 2:
            return vowel_count
    # If we've reached the end of the string without returning, it means no uppercase vowel was found.
    return 0
```

This script provides a function that solves the problem as stated in the original prompt. The function counts the number of uppercase vowels in even indices of the given string `s`. The total count is returned if the middle of the string is reached; otherwise, it continues to count until the end and returns 0 if no uppercase vowel in even indices is found. 

You can copy and paste this code block into a Python environment or script to use the `count_upper()` function as defined.