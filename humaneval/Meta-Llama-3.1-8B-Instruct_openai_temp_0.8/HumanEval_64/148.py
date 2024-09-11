### Solution: Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered
    a vowel when it is at the end of the given word.

    Args:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    s = s.lower()  # Convert to lowercase for consistency
    count = 0
    if s[-1] == 'y':  # Check if 'y' is at the end of the string
        vowels += 'y'
        s = s[:-1]  # Remove the last character ('y') for counting

    # Count vowels
    for char in s:
        if char in vowels:
            count += 1

    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("Yellow")) # Expected output: 3
```