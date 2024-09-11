```python
# Define the function vowels_count that takes a string as input and returns the count of vowels
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): The input string to count vowels in

    Returns:
    int: The number of vowels in the string
    """
    # Initialize count of vowels to 0
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y' or 'Y'
        if s[-1].lower() == 'y':
            # If the last character is 'y', add 1 to the count
            count += 1
        
        # Iterate through each character in the string
        for char in s:
            # Check if the character is a vowel (either lower or upper case)
            if char.lower() in 'aeiou':
                # If the character is a vowel, add 1 to the count
                count += 1
    
    # Return the count of vowels
    return count

# Test the function with example cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("AEIOU"))  # Expected output: 5
print(vowels_count("bcdfg"))  # Expected output: 0
print(vowels_count("A"))      # Expected output: 1
```

This script defines a function `vowels_count` that counts the number of vowels in a given string, considering 'y' as a vowel only when it's at the end of the string. It also includes test cases to verify the function's correctness.