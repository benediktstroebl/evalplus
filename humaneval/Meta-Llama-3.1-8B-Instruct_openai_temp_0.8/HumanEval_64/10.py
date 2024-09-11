```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given word.
    It considers 'a', 'e', 'i', 'o', 'u' as vowels and 'y' as a vowel
    if it is at the end of the word.

    Parameters:
    s (str): The input word.

    Returns:
    int: The number of vowels in the word.
    """
    # Convert the word to lower case to make the function case-insensitive
    s = s.lower()
    # Initialize a counter for vowels
    vowel_count = 0
    # Check if the word ends with 'y'
    is_word_y = s.endswith('y')
    # Remove the last character if the word ends with 'y' to avoid counting it as a vowel
    if is_word_y:
        s = s[:-1]
    # Count the number of vowels in the word
    for char in s:
        if char in 'aeiou':
            vowel_count += 1
    # If the word ended with 'y', add it to the count
    if is_word_y:
        vowel_count += 1
    return vowel_count

# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("Hello"))  # Expected output: 2
print(vowels_count("AEIOUy"))  # Expected output: 6
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. It first converts the input string to lower case to make the function case-insensitive. Then it checks if the word ends with 'y' and removes the last character if it does, to avoid counting it as a vowel. It then counts the number of vowels in the word and adds 1 to the count if the word ended with 'y'. Finally, it returns the count. The script includes test cases to demonstrate the function's behavior.