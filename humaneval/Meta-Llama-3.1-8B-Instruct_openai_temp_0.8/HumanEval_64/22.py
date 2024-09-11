```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase to handle uppercase letters
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If 'y' is at the end, count it as a vowel
            count += 1
        # Count the vowels 'a', 'e', 'i', 'o', 'u'
        for char in s:
            if char in 'aeiou':
                count += 1
                
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("Hello"))  # Expected output: 2
print(vowels_count("AEIOU"))  # Expected output: 5
print(vowels_count(""))       # Expected output: 0
print(vowels_count("y"))      # Expected output: 1
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, following the specified rules. The script includes test cases to verify the function's correctness.