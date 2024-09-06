```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels
    vowels = 'AEIOU'
    # Initialize the count to 0
    count = 0
    # Iterate through each character in the string
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` which takes a string as an argument and counts the number of uppercase vowels in even indices of that string. It returns the count of uppercase vowels in even indices of the string. The function relies on the modulus operator (`%`) to check if an index is even and uses the `isupper()` method along with `contains` to check if the character is an uppercase vowel. 

To test this script, you can call the function with different input strings and verify the returned counts with the expected results.