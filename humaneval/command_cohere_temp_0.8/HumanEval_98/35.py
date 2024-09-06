```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels to be counted
    vowels = 'AEIOU'
    
    # Initialize the count to 0
    count = 0
    
    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Check if the character is uppercase and a vowel
        if char.isupper() and char in vowels:
            # If the index is even, increment the count
            if i % 2 == 0:
                count += 1
    
    # Return the final count
    return count
```

To use this function, simply call it with a string as an argument, and it will return the number of uppercase vowels in even indices in the string. 

For example:
```python
print(count_upper('aBCdEf'))  # Output: 1
print(count_upper('abcdefg'))  # Output: 0
print(count_upper('dBBE'))  # Output: 0
```