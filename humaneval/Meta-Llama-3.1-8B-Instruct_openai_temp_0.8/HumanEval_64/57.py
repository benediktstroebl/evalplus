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
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiouy' and (s.index(char) == len(s) - 1 or char not in 'y'):
            # If it's a vowel, increment the counter
            vowel_count += 1
    
    # Return the total vowel count
    return vowel_count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

Note that I used `str.lower()` to convert the string to lowercase before processing it, which simplifies the problem slightly. This approach assumes that the input string contains only ASCII characters. If you need to support other character encodings (e.g., Unicode), you'll need to adjust the code accordingly.