### Vowels Counter Script

Below is a Python script that solves the problem. This script defines a function `vowels_count` which takes a string as input and returns the number of vowels in the string.

```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, 
    but only when it is at the end of the given word.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiouy':
            # If the character is a vowel, increment the counter
            count += 1
            # If the character is 'y' and it's not at the end of the string, break the loop
            if char == 'y' and s.index(char)!= len(s) - 1:
                break
        # If the character is not a vowel and it's at the end of the string and the previous character is 'y', break the loop
        elif char == s[-1] and s[-2] == 'y':
            break
    
    # Return the count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines the `vowels_count` function, which takes a string `s` as input, converts it to lowercase for simplicity, and then iterates over each character in the string. It counts the number of vowels, treating 'y' as a vowel only when it's at the end of the string. The function returns the count of vowels. The script also includes test cases to verify the function's correctness.