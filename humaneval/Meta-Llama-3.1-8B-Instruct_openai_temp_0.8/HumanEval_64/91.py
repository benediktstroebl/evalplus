### Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel if it's at the end of the word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.

    Example:
        >>> vowels_count("abcde")
        2
        >>> vowels_count("ACEDY")
        3
    """
    s = s.lower()
    count = 0
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Count the number of times each vowel appears in the string
    for char in s:
        if char in vowel_count:
            count += 1
            vowel_count[char] += 1

    # If 'y' is at the end of the word, add it to the count
    if s and s[-1] == 'y':
        count += 1

    return count
```
This script uses a dictionary to count the occurrences of each vowel in the string, then adds 1 to the count if 'y' is at the end of the string. The function is case-insensitive and returns the total count of vowels in the string.