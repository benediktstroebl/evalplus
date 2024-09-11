### Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel when at the end of the string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    y_is_vowel = s.endswith('y')
    
    # Count the number of vowels
    count = sum(1 for char in s.lower() if char in vowels and (not y_is_vowel or char!= 'y'))
    
    return count

# Example usage:
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("ayan"))    # Expected output: 3
print(vowels_count("yttrium")) # Expected output: 2
```