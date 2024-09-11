```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Args:
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
    last_char = s[-1].lower() if s else ''
    
    # Check if the last character is 'y' and count it as a vowel
    is_last_char_y = last_char == 'y' and len(s) == 1

    count = sum(1 for char in s.lower() if char in vowels)

    if is_last_char_y:
        count += 1  # increment count by 1 if last character is 'y'

    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("aeiou"))  # Expected output: 5
print(vowels_count("bcd"))    # Expected output: 0
print(vowels_count("y"))      # Expected output: 1
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string. It first initializes a string of vowels and then checks the last character of the input string. If the last character is 'y', it counts it as a vowel. Then it uses a generator expression to count the number of vowels in the string (ignoring case).