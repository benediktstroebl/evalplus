```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given word.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'.
    'y' is also considered a vowel when it's at the end of the word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase to handle both lowercase and uppercase vowels
    s = s.lower()
    # Initialize a counter for vowels
    count = 0
    # Check if the string is not empty
    if s:
        # Check if the string ends with 'y'
        if s[-1] == 'y':
            # If it ends with 'y', consider 'y' as a vowel
            vowels = 'aeiouy'
        else:
            # Otherwise, consider only 'a', 'e', 'i', 'o', 'u' as vowels
            vowels = 'aeiou'
        # Iterate over each character in the string
        for char in s:
            # Check if the character is a vowel
            if char in vowels:
                # If it's a vowel, increment the counter
                count += 1
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("AEIOU"))  # Expected output: 5
print(vowels_count("bcdfg"))  # Expected output: 0
print(vowels_count(""))       # Expected output: 0
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. The function first converts the string to lowercase to handle both lowercase and uppercase vowels. It then initializes a counter `count` to zero. If the string is not empty, it checks whether the string ends with 'y'. If it does, it considers 'y' as a vowel; otherwise, it considers only 'a', 'e', 'i', 'o', and 'u' as vowels. It then iterates over each character in the string, increments the `count` for each vowel it encounters, and returns the total count of vowels. The script includes several test cases to demonstrate the function's behavior.