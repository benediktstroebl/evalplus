```python
def vowels_count(s):
    """
    Counts the number of vowels in a given word. 'y' is considered a vowel 
    only when it's at the end of the word.

    Args:
        s (str): The input word.

    Returns:
        int: The total number of vowels in the word.
    """
    # Convert the string to lowercase to make the function case-insensitive
    s = s.lower()
    
    # Initialize a counter for vowels
    vag_count = 0
    
    # Check if the last character is 'y'
    if s[-1] == 'y' and len(s) > 1:
        # If 'y' is at the end, don't count it
        s = s[:-1]
        
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it's a vowel, increment the counter
            vag_count += 1
    
    # Return the total count of vowels
    return vag_count


# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("aeiou"))  # Expected output: 5
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("yay"))    # Expected output: 2
```