```python
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
    # Convert the string to lowercase to simplify the vowel check
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the counter
            count += 1
        elif char == 'y' and s.endswith(char):
            # If the character is 'y' and it is at the end of the string, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("AEIouY"))  # Output: 4
```

This script uses a simple loop to check each character in the input string. It counts the number of vowels (both lowercase and uppercase) and increments the counter when it encounters a vowel. It also checks for the special case where 'y' is a vowel when it is at the end of the string. The function returns the total count of vowels.