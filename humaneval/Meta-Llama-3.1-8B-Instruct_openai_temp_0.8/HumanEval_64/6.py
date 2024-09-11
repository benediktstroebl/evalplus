```python
def vowels_count(s):
    """
    Count the number of vowels in a given string.
    
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel if it is at the end of the word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = 'aeiou'  # Define vowels without 'y'
    end_y_vowel = 'y' if s[-1].lower() == 'y' else ''
    
    # Count the number of vowels in the string, including 'y' at the end
    count = sum(1 for char in s.lower() if char in vowels + end_y_vowel)
    
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("Hello World"))  # Expected output: 3
print(vowels_count("AEIOU"))  # Expected output: 5
print(vowels_count("y"))  # Expected output: 1
```

This script defines a function `vowels_count` that counts the number of vowels in a given string, including 'y' at the end of the string. The function uses a generator expression to iterate over the characters in the string, counting those that are vowels. The test cases at the end demonstrate the function's behavior with different inputs.