```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel, 
    but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase to simplify vowel detection
    s = s.lower()
    
    # Initialize a counter for the vowels and a flag to track if 'y' is at the end
    count = 0
    is_y_at_end = s.endswith('y')
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel (or 'y' if it's at the end)
        if char in 'aeiou' or (is_y_at_end and char == 'y'):
            # Increment the vowel counter if the character is a vowel
            count += 1
    
    # Return the total count of vowels
    return count

# Test the function with the provided example cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, considering the special case of 'y' at the end of the word. It then tests the function with the provided example cases.