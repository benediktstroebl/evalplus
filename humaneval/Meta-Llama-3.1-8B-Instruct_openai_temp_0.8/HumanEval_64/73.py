```markdown
### Vowels Count Function
#### Description
A function to count the number of vowels in a given string, where 'y' is a vowel only when it is at the end of the string.

#### Code
```python
def vowels_count(s):
    """
    Count the number of vowels in a string.
    
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character is 'y'
    if s and s[-1] == 'y':
        # If 'y' is at the end, increment the count
        count += 1
    
    # Count the occurrences of 'a', 'e', 'i', 'o', 'u'
    for char in s:
        if char in 'aeiou':
            count += 1
    
    return count
```

#### Example Use Cases
```python
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("yyy"))  # Output: 1
```

#### Note
This function has a time complexity of O(n), where n is the length of the input string, as it iterates over the string to count the occurrences of vowels.