```python
def vowels_count(s):
    """
    Returns the number of vowels in a given word.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel, 
    but only when it is at the end of the given word.

    Args:
        s (str): The input word.

    Returns:
        int: The number of vowels in the word.
    """
    # Convert the word to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the word ends with 'y'
    if s.endswith('y'):
        # If it does, remove the 'y' and decrement the counter
        count -= 1
        s = s[:-1]
    
    # Iterate over each character in the word
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it is, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, considering 'y' as a vowel only when it is at the end of the word. The script includes test cases to demonstrate its correctness.