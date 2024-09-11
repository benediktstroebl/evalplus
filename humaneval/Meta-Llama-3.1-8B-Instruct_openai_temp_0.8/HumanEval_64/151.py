```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel if it's at the end of the string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    y_at_end = 1 if s and s[-1].lower() == 'y' else 0
    
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Use a generator expression to count the vowels
    count = sum(1 for char in s if char in vowels)
    
    # Add 1 to the count if 'y' is at the end of the string
    count += y_at_end
    
    return count

# Example usage
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, following the specified rules. It uses a generator expression to count the vowels and takes into account the special case where 'y' is at the end of the string. The script also includes example usage to demonstrate the function's behavior.