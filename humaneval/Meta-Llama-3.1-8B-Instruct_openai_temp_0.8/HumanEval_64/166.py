```python
# Function to count the number of vowels in a given word
def vowels_count(s):
    """
    This function counts the number of vowels in a given word.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'y' is also considered a vowel if it's at the end of the word.

    Args:
        s (str): The input word.

    Returns:
        int: The number of vowels in the word.
    """
    # Convert the word to lowercase
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Initialize a flag to check if 'y' is at the end of the word
    y_at_end = s[-1] == 'y'
    
    # Iterate over each character in the word
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the counter
            count += 1
        elif char == 'y' and y_at_end:
            # If the character is 'y' and it's at the end of the word, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count

# Testing the function
print(vowels_count("abcde"))  # Expected output: 3
print(vowels_count("ACEDY"))  # Expected output: 3
```

This Python script defines a function `vowels_count` that counts the number of vowels in a given word. It considers 'y' as a vowel if it's at the end of the word. The function uses a simple loop to iterate over each character in the word and increments a counter whenever it encounters a vowel. Finally, it returns the total count of vowels.