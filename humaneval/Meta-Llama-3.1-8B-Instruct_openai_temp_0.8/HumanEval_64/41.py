```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string.
    
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is a vowel if it's at the end of the word.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    
    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    
    # Convert the string to lower case to simplify the vowel check
    s = s.lower()
    
    # Initialize a counter for the vowels
    count = 0
    
    # Iterate over each character in the string
    for i, char in enumerate(s):
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it's not at the end of the word, increment the counter
            if i!= len(s) - 1:
                count += 1
        # If the character is 'y' and it's at the end of the word, increment the counter
        elif char == 'y' and i == len(s) - 1:
            count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string, considering 'y' as a vowel if it's at the end of the word. It uses a simple loop to iterate over each character in the string and a counter to keep track of the vowels. The function is then tested with the provided example test cases.