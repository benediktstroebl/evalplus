### Vowels Count Function
```python
def vowels_count(s):
    """
    This function calculates the number of vowels in a given word.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel
    if it's at the end of the word.

    Args:
        s (str): The input word.

    Returns:
        int: The number of vowels in the word.
    """
    # Convert the string to lowercase to simplify vowel detection
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Initialize a flag to track if 'y' is at the end of the word
    y_at_end = False
    
    # Check if the word ends with 'y'
    if s.endswith('y'):
        # If it does, remove the last character
        s = s[:-1]
        # Set the flag to True
        y_at_end = True
    
    # Iterate over each character in the word
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it is, increment the vowel count
            count += 1
    
    # If 'y' was considered a vowel, increment the count one more time
    if y_at_end:
        count += 1
    
    # Return the total vowel count
    return count

# Test cases
print(vowels_count("abcde"))  # Expected: 2
print(vowels_count("ACEDY"))  # Expected: 3
print(vowels_count("hello"))  # Expected: 2
print(vowels_count("y"))      # Expected: 1
print(vowels_count("a"))      # Expected: 1
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string. The function considers 'y' as a vowel if it appears at the end of the word. It uses a simple looping approach to count the vowels and handles the special case of 'y' at the end of the word. The script also includes some test cases to verify the function's correctness.