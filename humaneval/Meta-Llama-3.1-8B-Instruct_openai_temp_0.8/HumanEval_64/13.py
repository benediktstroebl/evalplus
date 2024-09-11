```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): A string representing a word.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase to handle both uppercase and lowercase letters
    s = s.lower()
    # Initialize a counter for vowels
    count = 0
    # Check if the word is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If 'y' is at the end, count it as a vowel
            count += 1
        # Iterate over the characters in the string
        for char in s:
            # Check if the character is a vowel
            if char in 'aeiou':
                # If it's a vowel, increment the counter
                count += 1
    # Return the count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("aeiou"))  # Expected output: 5
print(vowels_count("bcd"))    # Expected output: 0
print(vowels_count("y"))      # Expected output: 1
```

This Python script defines a function `vowels_count` that implements the required logic to count the number of vowels in a given string. It handles both uppercase and lowercase letters by converting the input string to lowercase. The function also correctly counts 'y' as a vowel when it appears at the end of the string. The test cases at the end verify the correctness of the function.