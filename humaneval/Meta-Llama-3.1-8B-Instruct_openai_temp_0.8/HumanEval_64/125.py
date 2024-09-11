```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = 'aeiou'
    s = s.lower()  # convert the string to lowercase
    count = 0
    is_last_char_y = False  # flag to check if the last character is 'y'

    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            is_last_char_y = True
            s = s[:-1]  # remove the last character 'y'

    # Count the number of vowels
    for char in s:
        if char in vowels:
            count += 1

    # If the last character was 'y' and the word was not empty, add 1 to the count
    if is_last_char_y and s:
        count += 1

    return count


# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("aeiou"))  # Expected output: 5
print(vowels_count("bcdfg"))  # Expected output: 0
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string, considering 'y' as a vowel only when it is at the end of the word. The script also includes test cases to verify the correctness of the function.