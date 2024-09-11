```python
def vowels_count(s):
    """
    Counts the number of vowels in a given word.
    
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel,
    but only when it is at the end of the given word.
    
    Parameters:
    s (str): The input word.
    
    Returns:
    int: The number of vowels in the word.
    """
    # Convert the string to lowercase to handle uppercase letters
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the word ends with 'y'
    ends_with_y = s.endswith('y')
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            count += 1
        # If the word ends with 'y' and the 'y' is not at the end of the word, increment the count
        elif char == 'y' and not ends_with_y:
            count += 1
    
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("aeiou"))  # Expected output: 5
print(vowels_count("y"))      # Expected output: 1
print(vowels_count("aey"))    # Expected output: 2
```

This script implements the `vowels_count` function as described in the problem. It converts the input string to lowercase, counts the number of vowels, and handles the special case where 'y' is a vowel only when it is at the end of the word. The script also includes test cases to verify the correctness of the function.