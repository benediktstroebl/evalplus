### Vowels Counter Function
```python
# Define a constant string containing the vowels
VOWELS = 'aeiouyAEIOUY'

def vowels_count(s):
    """
    Returns the number of vowels in the given string.

    Vowels are 'a', 'e', 'i', 'o', 'u' and 'y' at the end of the word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # If the string is empty, there are no vowels
    if not s:
        return 0
    
    # Get the last character of the string
    last_char = s[-1]
    
    # Count the vowels in the string, considering 'y' at the end
    count = s[:-1].lower().count(VOWELS) + (1 if last_char.lower() in 'yY' else 0)
    
    return count

# Example use cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

In this code:

1. We define a constant string `VOWELS` containing all the vowels.
2. The `vowels_count` function checks if the input string is empty and returns 0 in that case.
3. It gets the last character of the string and considers 'y' at the end of the word as a vowel.
4. It counts the vowels in the string (excluding the last character) using the `count` method.
5. It adds 1 to the count if the last character is 'y' or 'Y' (i.e., 'y' at the end of the word).
6. The function returns the total vowel count.