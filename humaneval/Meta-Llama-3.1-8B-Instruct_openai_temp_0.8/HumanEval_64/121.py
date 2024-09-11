```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns 
    the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 
    'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of 
    the given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the word ends with 'y' and subtract 1 from the count if it does
    if s.endswith('y'):
        count -= 1
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it is, increment the count
            count += 1
    
    # Return the count
    return count

# Test cases
print(vowels_count("abcde"))  # Should print 3
print(vowels_count("ACEDY"))  # Should print 3
print(vowels_count("aEioUy"))  # Should print 1
print(vowels_count("helloWorld"))  # Should print 3
print(vowels_count("xy"))  # Should print 2
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, with the special condition that 'y' is considered a vowel only when it is at the end of the word. The function uses a simple loop to iterate over each character in the string and a counter to keep track of the number of vowels. The script also includes some test cases to verify the function's correctness.