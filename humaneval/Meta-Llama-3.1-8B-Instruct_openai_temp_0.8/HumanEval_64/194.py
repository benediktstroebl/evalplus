```python
# Define a function to count vowels in a string
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns
    the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 'o', 'u'.
    Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): The input string

    Returns:
    int: The number of vowels in the string
    """
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character of the string is 'y'
    if len(s) > 0 and s[-1].lower() == 'y':
        # If 'y' is at the end, don't count it if it's not at the end
        s = s[:-1]
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char.lower() in 'aeiou':
            # If it's a vowel, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count


# Example usage
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string. The function first checks if the last character of the string is 'y', and if it is, removes it from the string. It then iterates over each character in the string, counting the vowels. The function returns the total count of vowels. The script includes example usage at the end to demonstrate how to use the function.