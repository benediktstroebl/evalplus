```markdown
### Vowels Count Function

The following Python script provides a function `vowels_count` to count the number of vowels in a given word.

```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the input string to lowercase to handle case-insensitive input
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check each character in the string
    for char in s:
        # Check if the character is a vowel (excluding 'y' when it's not at the end)
        if char in 'aeiou' or (char == 'y' and s.endswith('y')):
            # Increment the vowel counter
            count += 1
    
    # Return the total count of vowels
    return count

# Example usage
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("Hello"))  # Output: 2
```

### Notes

* This function uses a simple loop to iterate over each character in the input string.
* It uses the `lower()` method to convert the input string to lowercase for case-insensitive counting.
* It checks each character to see if it's a vowel, using the `in` operator to check for membership in the string `'aeiou'`.
* If the character 'y' is encountered, it checks if the string ends with 'y' to determine if it should be counted as a vowel or not.
* The function returns the total count of vowels found in the string.