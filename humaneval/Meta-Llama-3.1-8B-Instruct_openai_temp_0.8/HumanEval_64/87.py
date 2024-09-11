```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns 
    the number of vowels in the string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a 
    vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Convert the string to lowercase to handle both lowercase and uppercase vowels
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Initialize a flag to track if 'y' is at the end of the string
    last_char_is_y = False
    
    # Check the last character of the string
    if s and s[-1] == 'y':
        # If the string is not empty and its last character is 'y', set the flag to True
        last_char_is_y = True
        
        # Remove the last character from the string
        s = s[:-1]
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the count
            count += 1
    
    # If 'y' was at the end of the string and was a vowel, increment the count
    if last_char_is_y:
        count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```
This script defines a function called `vowels_count` that takes a string as input and returns the total count of vowels in the string. The function handles both lowercase and uppercase vowels and also considers 'y' as a vowel if it is at the end of the string. The test cases are provided to demonstrate the function's correctness.