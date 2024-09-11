### Vowels Count Function
#### Problem Statement
Add a function `vowels_count` that takes a string representing a word as input and returns the number of vowels in the string.
#### Code
```python
def vowels_count(s: str) -> int:
    """
    Count the number of vowels in a given word.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'y' is also considered a vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input word.

    Returns:
        int: The number of vowels in the word.
    """
    # Convert the input string to lowercase for case-insensitive comparison
    s = s.lower()
    
    # Initialize the count of vowels to 0
    count = 0
    
    # Iterate over each character in the string
    for i, char in enumerate(s):
        # Check if the character is a vowel
        if char in 'aeiou':
            # Increment the count if the character is a vowel
            count += 1
        elif char == 'y' and i == len(s) - 1:
            # Increment the count if 'y' is at the end of the string
            count += 1
    
    # Return the total count of vowels
    return count
```

### Example Use Cases
```python
# Test the function with example inputs
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("y"))  # Output: 1
print(vowels_count("bcdfg"))  # Output: 0
```