```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): The input word.

    Returns:
    int: The number of vowels in the string.

    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = 'aeiou'
    s = s.lower()  # Convert the string to lowercase for simplicity
    count = 0
    # Check if the last character is 'y'
    if len(s) > 0 and s[-1] == 'y':
        vowels += 'y'  # If it is, add 'y' to the vowels string
    # Count the vowels
    for char in s:
        if char in vowels:
            count += 1
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("aeiou"))  # Expected output: 5
print(vowels_count("bcdfg"))  # Expected output: 0
print(vowels_count("y"))  # Expected output: 1
```
This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. It first converts the string to lowercase for simplicity, then checks if the last character is 'y' and adds it to the vowels string if it is. It then counts the occurrences of vowels in the string and returns the count. The script includes several test cases to verify the correctness of the function.