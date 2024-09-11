```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. However, 'y' is also considered a vowel if it is at the end of the word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the input string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character is 'y' and increment the count if it is
    if len(s) > 0 and s[-1] == 'y':
        count += 1
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel and increment the count if it is
        if char in 'aeiou':
            count += 1
    
    # Return the total count of vowels
    return count
```

Here are some example use cases for the `vowels_count` function:

```python
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("yay"))    # Output: 1
print(vowels_count(""))       # Output: 0
```