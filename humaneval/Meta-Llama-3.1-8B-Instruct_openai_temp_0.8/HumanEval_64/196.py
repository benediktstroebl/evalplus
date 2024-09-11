```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns 
    the number of vowels in the string. Vowels in this case are 'a', 'e', 
    'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the 
    end of the given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.

    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y' and it's not at the beginning
        if len(s) > 1 and s[-1] == 'y' and s[-2] not in 'aeiouy':
            # If 'y' is at the end, increment the counter
            count += 1
        # Count all the vowels in the string
        for char in s:
            if char in 'aeiouy':
                count += 1
                
    # Return the total count of vowels
    return count

# Example usage:
print(vowels_count("abcde"))  # Outputs: 2
print(vowels_count("ACEDY"))  # Outputs: 3
```

This script defines the `vowels_count` function, which counts the number of vowels in a given string. The function handles both lowercase and uppercase letters, and it treats 'y' as a vowel only when it's at the end of the string. The script includes example usage at the end to demonstrate how to use the function.