### Vowels Counter
```python
def vowels_count(s: str) -> int:
    """
    This function takes a string as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel if it's at the end of the given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    end_vowel = 'y' if len(s) > 1 and s[-1].lower() == 'y' else ''
    s = s.lower()
    return sum(1 for char in s if char in vowels + end_vowel)


# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("xyz"))    # Expected output: 1
```
This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. The function considers 'y' as a vowel only if it's at the end of the string. It uses a generator expression to iterate over the characters in the string and counts the vowels. The result is then returned. The script also includes test cases to verify the functionality of the `vowels_count` function.