### Vowels Counter Function
```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns
    the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 'o', 'u'.
    'Y' is also a vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the input string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the counter
            count += 1
        elif char == 'y' and s.endswith('y'):
            # If the character is 'y' and it's at the end of the string, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```
In this code, we define a function `vowels_count` that takes a string `s` as input. We convert the string to lowercase to simplify the vowel check. We then iterate over each character in the string, checking if it's a vowel or 'y' at the end of the string. We increment the counter accordingly and return the total count of vowels at the end.