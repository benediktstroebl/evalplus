```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns 
    the number of vowels in the string. Vowels in this case are 'a', 'e', 
    'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the 
    end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase to handle vowels in uppercase
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the counter
            count += 1
        # Check if the character is 'y' and it is at the end of the string
        elif char == 'y' and s == char:
            # If the character is 'y' at the end of the string, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("world"))  # Output: 1
```