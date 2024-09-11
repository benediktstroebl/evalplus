### Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in a given string.
    Vowels are 'a', 'e', 'i', 'o', 'u' and 'y' at the end of the word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase to simplify vowel detection
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou' or (char == 'y' and s.endswith(char)):
            # If it is, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count

# Example use cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```
This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. The function converts the input string to lowercase to simplify vowel detection, initializes a counter for vowels, and checks each character in the string to see if it is a vowel. If the character is a vowel, the counter is incremented. Finally, the function returns the total count of vowels.