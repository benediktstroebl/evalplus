```python
def vowels_count(s):
    """
    Counts the number of vowels in a given word.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel
    if it appears at the end of the given word.

    Args:
        s (str): The input word.

    Returns:
        int: The number of vowels in the word.
    """
    # Convert the string to lowercase to simplify the vowel check
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check each character in the string
    for i, char in enumerate(s):
        # If the character is a vowel (including 'y' at the end)
        if char in 'aeiou' or (char == 'y' and i == len(s) - 1):
            # Increment the vowel count
            count += 1
    
    # Return the total vowel count
    return count

# Test the function
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This script defines a function `vowels_count` that takes a string as input and returns the count of vowels in it. The function handles both lowercase and uppercase vowels correctly and also treats 'y' as a vowel if it's at the end of the word. The script includes test cases to demonstrate the function's correctness.