```python
# Define the function vowels_count to count the number of vowels in a given string
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    Here, 'y' is also a vowel, but only when it is at the end of the given word.
    
    Parameters:
    s (str): The input string to count vowels from.
    
    Returns:
    int: The total number of vowels in the string.
    """
    
    # Convert the input string to lowercase to simplify vowel checking
    s = s.lower()
    
    # Initialize a counter variable to store the total number of vowels
    vowel_count = 0
    
    # Iterate over each character in the input string
    for i, char in enumerate(s):
        # Check if the character is a vowel or 'y' at the end of the string
        if char in 'aeiou' or (char == 'y' and i == len(s) - 1):
            # If the character is a vowel or 'y' at the end, increment the vowel counter
            vowel_count += 1
    
    # Return the total number of vowels found in the string
    return vowel_count

# Test the function with example inputs
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines the `vowels_count` function, which takes a string input and returns the number of vowels in the string. It utilizes the properties described in the problem statement, including considering 'y' as a vowel only when it's at the end of the string. The script includes example test cases to demonstrate its functionality.