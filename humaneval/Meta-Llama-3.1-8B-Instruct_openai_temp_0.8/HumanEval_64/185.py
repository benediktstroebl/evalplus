### Vowels Count Function
#### Problem Description
The following Python function calculates the number of vowels in a given string. Vowels are 'a', 'e', 'i', 'o', 'u' but 'y' is also considered a vowel when it's at the end of the word.

```python
def vowels_count(s):
    """
    Calculate the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel
    when it's at the end of the word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lower case for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the string is not empty
    if s:
        # Count the vowels
        for char in s:
            if char in 'aeiouy' and (s.index(char) == len(s) - 1 or not char == 'y'):
                count += 1
            elif char in 'aeiou' and s.index(char)!= len(s) - 1:
                count += 1
                
    # Return the count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("Hello"))  # Expected output: 2
print(vowels_count(""))        # Expected output: 0
print(vowels_count("a"))       # Expected output: 1
```

This script includes the `vowels_count` function as per the provided specification. It counts the number of vowels in a given string, considering 'y' as a vowel when it's at the end of the word. The function then tests with various input cases.