```python
def vowels_count(s):
    """
    Count the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel if it's at the end of the string.
    
    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    vowels = 'aeiou'  # Define vowels without 'y'
    end_with_y = len(s) > 0 and s[-1].lower() == 'y'  # Check if the string ends with 'y'
    extra_vowel = end_with_y and 'y' not in vowels  # Add 'y' as a vowel if it is at the end and is not already in the vowels string

    vowels += 'y' if extra_vowel else ''  # Update vowels string to include 'y' if it's an extra vowel

    return sum(1 for char in s.lower() if char in vowels)  # Count the vowels in the string, case-insensitive

# Example usage
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```
This script first initializes a string `vowels` containing all the vowels except 'y'. It then checks if the string ends with 'y'. If it does and 'y' is not already included in the `vowels` string, it treats 'y' as a vowel. The `sum` function is used with a generator expression to iterate over the characters in the string, counting the number of vowels. The result is returned as the number of vowels in the string.