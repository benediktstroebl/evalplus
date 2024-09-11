```python
def vowels_count(s):
    """
    This function takes a string as input and returns the number of vowels in the string.
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
    count = 0
    if s:  # Check if the string is not empty
        if s[-1].lower() == 'y':  # Check if the last character is 'y'
            vowels += 'y'
        for char in s.lower():  # Convert the string to lowercase
            if char in vowels:  # Check if the character is a vowel
                count += 1
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```
This script defines the `vowels_count` function as per the problem description. It first checks if the string is not empty and if the last character is 'y'. If so, it adds 'y' to the vowels string. Then it iterates over the string, converting it to lowercase, and increments the count whenever it encounters a vowel. Finally, it returns the count of vowels in the string. The test cases are also included at the end of the script.