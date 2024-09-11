```python
def vowels_count(s):
    """
    Counts the number of vowels in a given word.
    
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel only when it is at the end of the word.
    
    Parameters:
    s (str): The input string representing a word.
    
    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase to handle both lowercase and uppercase vowels
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Iterate over each character in the string
    for i, char in enumerate(s):
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the counter
            count += 1
        # Check if the character is 'y' and it's at the end of the string
        elif char == 'y' and i == len(s) - 1:
            # If the character is 'y' at the end, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("aeiou"))  # Expected output: 5
print(vowels_count("bcdfg"))  # Expected output: 0
print(vowels_count("y"))      # Expected output: 1
print(vowels_count("helloY")) # Expected output: 2
```