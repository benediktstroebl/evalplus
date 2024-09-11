```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'Y' is also a vowel if it's at the end of the word.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase to make the check case-insensitive
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character is 'y' and increment the count if it is
    if len(s) > 0 and s[-1] == 'y':
        count += 1
    
    # Iterate over the characters in the string
    for char in s:
        # Check if the character is a vowel and increment the count if it is
        if char in 'aeiou':
            count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("aeiou"))  # Expected output: 5
print(vowels_count("bcdfg"))  # Expected output: 0
```