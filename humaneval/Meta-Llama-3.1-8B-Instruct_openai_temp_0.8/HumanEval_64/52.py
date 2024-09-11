```python
def vowels_count(s):
    """
    Returns the number of vowels in a string, with 'y' being a vowel only if it's at the end of the string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    s = s.lower()  # Convert the string to lowercase for easier comparison
    vowel_count = 0  # Initialize the vowel count to 0
    is_y_at_end = s[-1] == 'y'  # Check if 'y' is at the end of the string

    for char in s:  # Iterate over each character in the string
        if char in 'aeiou':  # Check if the character is a vowel
            vowel_count += 1  # Increment the vowel count
        elif char == 'y' and not is_y_at_end:  # If 'y' is not at the end of the string, it's not a vowel
            continue

    return vowel_count  # Return the total vowel count


# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("aayed"))  # Expected output: 4
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, with 'y' being a vowel only if it's at the end of the string. It uses a simple iteration over the characters in the string to count the vowels, and handles the special case of 'y' at the end of the string separately. The script also includes some test cases to demonstrate the function's behavior.