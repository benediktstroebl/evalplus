```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string. Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'Y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If the last character is 'y', treat it as a vowel
            count += 1
            # Remove the last character to avoid counting 'y' twice
            s = s[:-1]
        
        # Iterate over each character in the string
        for char in s:
            # Check if the character is a vowel
            if char in 'aeiou':
                # If the character is a vowel, increment the counter
                count += 1
    
    # Return the total count of vowels
    return count

# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```