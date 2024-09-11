```python
# Define the function vowels_count
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns
    the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 'o', 'u'.
    Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Initialize a counter for vowels
    count = 0
    
    # Check if the word is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1].lower() == 'y':
            # Count 'y' as a vowel if it's at the end of the word
            count += 1
        
        # Count 'a', 'e', 'i', 'o', 'u' as vowels
        for char in s:
            if char.lower() in 'aeiou':
                count += 1
    
    # Return the total count of vowels
    return count

# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count(""))        # Expected output: 0
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string according to the specified rules. It then tests the function with several example cases.