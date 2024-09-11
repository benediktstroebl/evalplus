```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel if it's at the end of the string.

    Args:
        s (str): The input string.

    Returns:
        int: The count of vowels in the string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize the count of vowels to 0
    count = 0
    
    # Check if the last character is 'y' which is a vowel if it's at the end of the string
    if s and s[-1] == 'y':
        count += 1
    
    # Iterate over each character in the string
    for char in s:
        # If the character is a vowel, increment the count
        if char in 'aeiou':
            count += 1
    
    # Return the count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("aeiou"))  # Expected output: 5
print(vowels_count("Hello World"))  # Expected output: 3
print(vowels_count("y"))  # Expected output: 1
```

In this script, the `vowels_count` function takes a string `s` as input and returns the number of vowels in the string. It first converts the string to lowercase for simplicity and then checks if the last character is 'y' (a vowel if it's at the end of the string). It then iterates over each character in the string and increments the count if the character is a vowel. Finally, it returns the count of vowels.