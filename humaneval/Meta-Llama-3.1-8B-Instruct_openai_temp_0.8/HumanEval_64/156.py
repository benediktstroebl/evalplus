```python
def vowels_count(s):
    """
    This function takes a string as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel when it's at the end of the word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    s = s.lower()  # Convert the string to lowercase for simplicity
    vowels = "aeiou"
    count = 0
    last_char = s[-1] if len(s) > 0 else ""
    
    # Count regular vowels
    for char in s:
        if char in vowels:
            count += 1
    
    # If 'y' is at the end of the word, also count it as a vowel
    if last_char == 'y':
        count += 1
    
    return count

# Example use cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("y"))  # Expected output: 1
```

This script implements the `vowels_count` function as described in the problem statement. It first converts the input string to lowercase, then counts the occurrences of regular vowels. If the last character of the string is 'y', it increments the count by 1. Finally, it returns the total count of vowels in the string. The example use cases demonstrate the function's behavior with different inputs.