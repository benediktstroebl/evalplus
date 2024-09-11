```python
def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize count for vowels
    count = 0
    
    # Check if 'y' is at the end of the string
    end_with_y = s.endswith('y')
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            count += 1
        # If 'y' is at the end of the string, don't count it
        elif char == 'y' and not end_with_y:
            continue
    
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

In this script, the `vowels_count` function takes a string as input, converts it to lowercase, and initializes a count for vowels. It then iterates over each character in the string, counting the vowels and ignoring 'y' if it's not at the end of the string. The function returns the total count of vowels. The script includes two test cases to demonstrate its functionality.