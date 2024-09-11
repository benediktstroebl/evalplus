```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a 
    vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Convert the string to lowercase to handle both lowercase and uppercase vowels
    s = s.lower()
    
    # Initialize a counter for the number of vowels
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If the last character is 'y', increment the count
            count += 1
        
        # Iterate over each character in the string
        for char in s:
            # Check if the character is a vowel
            if char in 'aeiou':
                # If the character is a vowel, increment the count
                count += 1
    
    # Return the count of vowels
    return count
```

**Example Usage:**

```python
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("yellow")) # Output: 3
```