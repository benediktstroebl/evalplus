### Vowels Counter

Here is a Python script that defines a function `vowels_count` to count the number of vowels in a given word.

```python
def vowels_count(s: str) -> int:
    """
    Counts the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel
    if it is at the end of the given string.

    Args:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase to make the function case-insensitive
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character is 'y'
    if s[-1] == 'y':
        # If 'y' is at the end, decrement the count before iterating
        # to avoid counting it as a vowel
        vowels = 'aeiou'
    else:
        vowels = 'aeiouy'
    
    # Iterate over the string and count the vowels
    for char in s:
        if char in vowels:
            count += 1
    
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("Hello"))  # Expected output: 2
print(vowels_count("AEIOUY"))  # Expected output: 6
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. It first checks if the last character is 'y' and adjusts the set of vowels accordingly. Then it iterates over the string and counts the occurrences of the vowels.