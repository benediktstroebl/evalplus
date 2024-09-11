```python
def vowels_count(s):
    """
    This function takes a string representing a word as input, 
    and returns the number of vowels in the string. 
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'Y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): A string representing a word.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase to handle both lowercase and uppercase vowels
    s = s.lower()
    
    # Initialize a counter for the vowels
    count = 0
    
    # Iterate over each character in the string
    for i in range(len(s)):
        # Check if the character is a vowel
        if s[i] in 'aeiou':
            # If the character is a vowel, increment the counter
            count += 1
        # Check if the character is 'y' and it's at the end of the string
        elif s[i] == 'y' and i == len(s) - 1:
            # If the character is 'y' at the end of the string, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count

# Example usage
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

Note that this implementation handles both lowercase and uppercase vowels by converting the input string to lowercase. It also checks if 'y' is at the end of the string to follow the problem's rules. The example usage demonstrates how to call the function with different inputs and print the results.