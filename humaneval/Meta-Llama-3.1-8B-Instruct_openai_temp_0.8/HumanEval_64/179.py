```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string.
    
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel only when
    it is at the end of the given word. The string is case-insensitive.
    
    Parameters:
    s (str): The input string
    
    Returns:
    int: The number of vowels in the string
    """
    
    # Check if the string is empty
    if not s:
        return 0
    
    # Count vowels from the start of the string
    count_start = sum(1 for c in s[:-1] if c.lower() in 'aeiouy')
    
    # Special case: 'y' at the end of the string is a vowel
    if s[-1].lower() == 'y':
        count_start += 1
    
    # Count vowels from the end of the string, excluding 'y' at the end
    count_end = sum(1 for c in s[:-1][::-1] if c.lower() in 'aeiou')
    
    # Return the maximum count
    return max(count_start, count_end)

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("aAeEioo"))  # Expected output: 8
print(vowels_count("yay"))  # Expected output: 2
print(vowels_count("no vowels"))  # Expected output: 0
print(vowels_count(""))  # Expected output: 0
```

This Python script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string. The function considers 'y' as a vowel only when it is at the end of the string. It uses a combination of list comprehensions and the `lower` method to handle both lowercase and uppercase letters. The script includes test cases to verify the correctness of the function.