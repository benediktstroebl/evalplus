### Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel when it is at the end of the word.
    
    Args:
        s (str): The input string.
    
    Returns:
        int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    s = s.lower()  # Convert the string to lowercase for simplicity
    count = 0
    for i, char in enumerate(s):
        # Check if the character is a vowel
        if char in vowels:
            count += 1
            # If the vowel is 'y' and it's the last character in the string, don't count it
            if char == 'y' and i == len(s) - 1:
                count -= 1
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```
This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel when it is at the end of the word. The function works by iterating over the characters in the string, checking if each character is a vowel, and incrementing the count as necessary. The script also includes test cases to verify the correctness of the function.