### Vowels Count Function

Below is a Python function that satisfies the given specifications:

```python
def vowels_count(s):
    """
    This function calculates the number of vowels in a given word.

    Args:
        s (str): A string representing a word.

    Returns:
        int: The number of vowels in the string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'Y' is also a 
    vowel, but only when it is at the end of the given word.
    """
    vowels = 'aeiouy'
    # Convert the input string to lowercase to simplify the comparison
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in vowels:
            # If the character is 'y' and it's not at the end of the string, skip it
            if char == 'y' and s.index(char)!= len(s) - 1:
                continue
            # If the character is a vowel, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This function uses a simple iterative approach to count the vowels in the given word. It iterates over each character in the string, checks if it's a vowel, and increments the counter accordingly. If the vowel is 'y' and it's not at the end of the string, it skips it. The function finally returns the total count of vowels.