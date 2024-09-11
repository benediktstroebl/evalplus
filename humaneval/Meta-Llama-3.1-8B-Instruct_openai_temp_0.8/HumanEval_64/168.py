```python
# vowels_count.py
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Args:
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
    
    # Initialize a counter variable to store the number of vowels
    count = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel or 'y' at the end of the string
        if char in 'aeiou' or (char == 'y' and s.endswith(char)):
            # If the character is a vowel or 'y', increment the counter
            count += 1
    
    # Return the total count of vowels
    return count

# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```