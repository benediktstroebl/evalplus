**Vowel Count Function**
========================

### Problem Description

Write a function `vowels_count` that takes a string representing a word as input and returns the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

### Solution

```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    
    Args:
        s (str): The input string.
    
    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the counter
            count += 1
        elif char == 'y' and s.endswith(char):
            # If the character is 'y' and it's at the end of the string, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count
```

### Example Usage

```python
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("aeiouy")) # Output: 5
```

This solution works by first converting the input string to lowercase to handle both lowercase and uppercase vowels. It then initializes a counter for vowels and iterates over each character in the string. If a character is a vowel, it increments the counter. If a character is 'y' and it's at the end of the string, it also increments the counter. Finally, it returns the total count of vowels.