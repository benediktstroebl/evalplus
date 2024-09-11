### Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in a given string.

    A vowel is 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel, but only
    when it is at the end of the given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.

    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = 'aeiou'
    # Check if the string is not empty
    if s:
        # Count the vowels in the string
        count = sum(1 for char in s.lower() if char in vowels)
        # If the last character is 'y', it's a vowel
        if s[-1] == 'y':
            count += 1
        return count
    else:
        return 0

# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello world"))  # Expected output: 3
print(vowels_count(""))  # Expected output: 0
```

In the above script, we define a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. We use the `sum` function and a generator expression to count the vowels, which are defined as 'a', 'e', 'i', 'o', 'u'. We also check if the last character of the string is 'y', in which case it's a vowel. We then use some test cases to demonstrate the function's behavior.