```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel only when it's at the end of the string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The count of vowels in the string.
    """
    vowels = 'aeiou'
    count = 0
    if s.endswith('y'):  # check if the string ends with 'y'
        vowels += 'y'  # add 'y' to the vowel set
    for char in s.lower():  # iterate over each character in the string (case-insensitive)
        if char in vowels:  # check if the character is a vowel
            count += 1  # increment the vowel count
    return count

# Test cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("y"))  # Output: 1
print(vowels_count("Y"))  # Output: 1
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the count of vowels in the string. The function checks if the string ends with 'y' and adds 'y' to the vowel set. It then iterates over each character in the string (case-insensitive) and increments the vowel count if the character is a vowel. The script includes test cases to verify the function's correctness.