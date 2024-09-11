### Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel if it's at the end.

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
    vowels = 'aeiou'  # Define the set of vowels
    end_y = 0  # Flag to check if the last character is 'y'

    # Check if the last character is 'y'
    if s.endswith('y'):
        end_y = 1

    # Initialize the count of vowels
    count = 0

    # Iterate over the input string
    for char in s:
        # Check if the character is a vowel or 'y' at the end
        if char.lower() in vowels or (char.lower() == 'y' and end_y):
            count += 1

    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("aeiou"))  # Expected output: 5
```
This script defines the `vowels_count` function, which takes a string as input and returns the count of vowels in the string. It checks for 'y' at the end of the string separately to ensure it's counted as a vowel. The function is then tested with various input strings to demonstrate its correctness.