### Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is a vowel if it's at the end of the string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase to make the function case-insensitive
    s = s.lower()
    
    # Initialize the vowel count to 0
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If it is, increment the count
            count += 1
        # Iterate over each character in the string
        for char in s:
            # Check if the character is a vowel
            if char in 'aeiou':
                # If it is, increment the count
                count += 1
    
    # Return the vowel count
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("world"))  # Expected output: 1
print(vowels_count("ay"))     # Expected output: 1
print(vowels_count("yay"))    # Expected output: 2
```
This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. The function first converts the string to lowercase to make it case-insensitive. It then checks if the last character of the string is 'y' and increments the count if it is. Finally, it iterates over each character in the string and increments the count if the character is a vowel. The function returns the vowel count.

The script also includes test cases to demonstrate the function's behavior.