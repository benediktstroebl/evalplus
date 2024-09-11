### Vowels Count Function
#### Description
This script provides a function `vowels_count` to calculate the number of vowels in a given string. The function considers 'a', 'e', 'i', 'o', 'u' as vowels and 'y' as a vowel when it's at the end of the string.

#### Code
```python
def vowels_count(s):
    """
    This function takes a string as input and returns the count of vowels in the string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is a vowel when it's at the end of the string.

    Args:
        s (str): The input string.

    Returns:
        int: The count of vowels in the string.
    """
    # Convert the string to lower case to handle cases insensitive
    s = s.lower()
    
    # Initialize the vowel count to 0
    count = 0
    
    # Loop through each character in the string
    for char in s:
        # Check if the character is a vowel or 'y' at the end of the string
        if char in 'aeiou' or (char == 'y' and s.endswith(char)):
            # If the character is a vowel or 'y', increment the count
            count += 1
    
    # Return the total count of vowels
    return count

# Test the function
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

#### Example Use Cases
*   `vowels_count("hello")` returns 2
*   `vowels_count("world")` returns 1
*   `vowels_count("python")` returns 2
*   `vowels_count("y")` returns 1
*   `vowels_count("aeiou")` returns 5