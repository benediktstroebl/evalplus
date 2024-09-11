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
    vowels = 'aeiou'
    count = 0
    # Check if the word is empty
    if not s:
        return 0
    
    # Check if 'y' is at the end of the word and add its count
    if s[-1].lower() == 'y':
        count += 1

    # Count the vowels in the rest of the word
    for char in s:
        if char.lower() in vowels:
            count += 1

    return count

# Test cases
print(vowels_count("abcde"))  # Expected: 2
print(vowels_count("ACEDY"))  # Expected: 3
print(vowels_count(""))       # Expected: 0
print(vowels_count("ey"))     # Expected: 2
print(vowels_count("bcdf"))   # Expected: 0
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. The function checks if the word is empty and returns 0 in this case. It also checks if 'y' is at the end of the word and adds its count. Then it counts the vowels in the rest of the word and returns the total count. The script includes test cases to demonstrate the function's behavior.