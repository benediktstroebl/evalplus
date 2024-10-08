### Vowels Count Function
```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel only if it's at the end of the string.
    
    Args:
        s (str): The input string.
    
    Returns:
        int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    s = s.lower()  # Convert the string to lowercase for simplicity
    
    # Count the number of vowels
    count = sum(1 for char in s if char in vowels)
    
    # If the string ends with 'y', add 1 to the count
    if s and s[-1] == 'y':
        count += 1
    
    return count

# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("world"))  # Expected output: 1
print(vowels_count("y"))      # Expected output: 1
print(vowels_count(""))       # Expected output: 0
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, considering 'y' as a vowel only if it's at the end. It uses a generator expression to count the number of vowels in the string, and checks if the string ends with 'y' to add 1 to the count if necessary. The script also includes some test cases to demonstrate the function's behavior.