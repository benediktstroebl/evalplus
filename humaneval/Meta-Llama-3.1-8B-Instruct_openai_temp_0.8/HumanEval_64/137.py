```python
def vowels_count(s: str) -> int:
    """
    This function calculates the number of vowels in a given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is a vowel if it's at the end of the word.
    
    Parameters:
    s (str): The input string
    
    Returns:
    int: The number of vowels in the string
    """
    # Convert the string to lowercase to simplify the vowel check
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check each character in the string
    for char in s:
        # Check if the character is a vowel or 'y' at the end of the word
        if char in 'aeiou' or (char == 'y' and s[-1] == 'y'):
            # If it is, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde")) # Expected output: 2
print(vowels_count("ACEDY")) # Expected output: 3
print(vowels_count("hello")) # Expected output: 2
print(vowels_count("y")) # Expected output: 1
print(vowels_count("")) # Expected output: 0
```

This script defines the `vowels_count` function, which takes a string `s` as input and returns the number of vowels in the string. It handles the special case where 'y' is a vowel if it's at the end of the word. The function is then tested with some example use cases.