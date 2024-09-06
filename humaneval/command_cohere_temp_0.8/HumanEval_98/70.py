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
    for i, char in enumerate(s):
        # Check if the character is uppercase and a vowel
        if char.isupper() and char in vowels and (i % 2 == 0):
            # Increment the count by 1 if the conditions are met
            count += 1
    # Return the count of uppercase vowels in even indices
    return count
```

The code defines a function `count_upper()` which takes a string as an argument and counts the number of uppercase vowels in even indices of the string. It first creates a boolean list `vowels` containing the uppercase vowels 'AEIOU' to use for comparison. It then iterates through the characters of the input string, checking if each character is uppercase and a vowel, and whether its index is even. If all conditions are met, the count is incremented by 1, and finally, the total count is returned. 

To ensure correctness, the code only considers uppercase vowels and counts them only if they appear in an even index of the string. Thus, the provided example test cases return 1 for 'aBCdEf', 0 for 'abcdefg' and 0 for 'dBBE', as required.