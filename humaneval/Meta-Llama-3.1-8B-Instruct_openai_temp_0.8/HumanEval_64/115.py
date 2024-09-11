```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.

    Examples:
        >>> vowels_count("abcde")
        2
        >>> vowels_count("ACEDY")
        3
    """
    # Convert the string to lowercase to simplify the vowel check
    s = s.lower()
    
    # Initialize a counter for the vowels
    count = 0
    
    # Initialize a flag to check if the word ends with 'y'
    ends_with_y = False
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If the last character is 'y', set the flag to True
            ends_with_y = True
            # Remove the last character from the string
            s = s[:-1]
        
        # Iterate over each character in the string
        for char in s:
            # Check if the character is a vowel
            if char in 'aeiou':
                # If the character is a vowel, increment the counter
                count += 1
        # If the word ends with 'y', increment the counter
        if ends_with_y:
            count += 1
    
    # Return the total count of vowels
    return count
```