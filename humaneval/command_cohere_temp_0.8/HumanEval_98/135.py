```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels
    vowels = 'AEIOU'
    # Initialize the count to 0
    count = 0
    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Check if the character is uppercase and a vowel
        if char.isupper() and char in vowels:
            # Check if the index is even, increment the count if it is
            if i % 2 == 0:
                count += 1
    # Return the count of uppercase vowels in even indices
    return count
```

The code defines a function `count_upper()` which takes a string as an input and counts the number of uppercase vowels in even indices. It first defines a string `vowels` containing all the uppercase vowels. It then initializes a counter `count` to 0. Then it iterates through each character of the input string `s` using a for loop. For each character, it checks if the character is uppercase and a vowel at the same time. If the condition is met, it further checks if the index of the character is even. If it is, the counter is incremented. Finally, the function returns the pre-initialized counter.

Note that this solution uses only Python standard library and doesn't depend on external packages.