### Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in a given string.
    
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is a vowel when it's at the end of the word.
    
    Parameters:
    s (str): The input string to count vowels in.
    
    Returns:
    int: The number of vowels in the string.
    """
    s = s.lower()  # Convert the string to lowercase for simplicity
    vowels = 'aeiou'
    y_count = 0  # Initialize a variable to count 'y' at the end of the word
    
    if s and s[-1] == 'y':  # Check if the word ends with 'y'
        y_count = 1
    
    return sum(1 for char in s if char in vowels) + y_count  # Count vowels and add 'y' count if applicable

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("worldy"))  # Expected output: 2
print(vowels_count(""))  # Expected output: 0
```
This script defines a `vowels_count` function that takes a string `s` as input and returns the number of vowels in the string, considering 'y' as a vowel only when it's at the end of the word. The function converts the input string to lowercase for simplicity and counts the vowels by iterating over the characters in the string. It also handles edge cases, such as an empty string. The script includes test cases to demonstrate the function's behavior.