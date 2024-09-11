```python
def vowels_count(s):
    """
    Counts the number of vowels in a given word.
    
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'y' is also considered a vowel when it is at the end of the given word.

    Args:
        s (str): The input word.

    Returns:
        int: The number of vowels in the word.
    """
    # Convert the string to lowercase to simplify the condition
    s = s.lower()
    
    # Count the number of vowels and 'y' at the end of the word
    vowels = sum(1 for char in s if char in 'aeiou' or (char == 'y' and s.endswith(char)))
    
    return vowels

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This script defines the `vowels_count` function as specified in the problem. It converts the input string to lowercase to simplify the condition, then counts the number of vowels and 'y' at the end of the word using a generator expression and the `sum` function. Finally, it provides example usage of the function.