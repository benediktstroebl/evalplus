```python
# Define a function vowels_count that counts the vowels in a given string
def vowels_count(s):
    """
    Counts the vowels in a given string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase to simplify vowel detection
    s = s.lower()
    
    # Define the vowels
    vowels = 'aeiou'
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If 'y' is at the end, add 1 to the count
            count += 1
        
        # Iterate over each character in the string
        for char in s:
            # Check if the character is a vowel
            if char in vowels:
                # If the character is a vowel, increment the count
                count += 1
    
    # Return the total count of vowels
    return count

# Example use cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. It first converts the string to lowercase to simplify vowel detection, then checks if the last character is 'y'. If 'y' is at the end, it adds 1 to the count. It then iterates over each character in the string and increments the count whenever it encounters a vowel. Finally, it returns the total count of vowels in the string.