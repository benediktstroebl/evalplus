### Vowels Count Function
```python
# Define a string of vowels and a string of characters considered vowels when at the end of a word
VOWELS = "aeiouAEIOU"
END_VOWEL = "yY"

def vowels_count(s):
    """
    Count the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u' and 'y' when at the end of the word.

    Args:
        s (str): Input string to count vowels in.

    Returns:
        int: Number of vowels in the string.
    """
    # Count the number of vowels in the string
    count = sum(1 for char in s if char in VOWELS)
    
    # If the string ends with 'y', add 1 to the count
    if s and s[-1] in END_VOWEL:
        count += 1
    
    return count
```

### Example Use Cases
```python
# Test the function with examples
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("helloY")) # Expected output: 3
```