```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels
    vowels = set(['A', 'E', 'I', 'O', 'U'])
    # Initialize the counter
    count = 0
    # Iterate through the string
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` which accepts a string `s` as an argument and returns the number of uppercase vowels in even indices of that string. The function first creates a set of uppercase vowels and initializes a count variable to 0. It then iterates through the string, checking if each character is an uppercase vowel and if it is located at an even index. If both conditions are met, the count variable is incremented. Finally, the function returns the count variable. 

The operation of the function is illustrated by the tests provided:
```python
# Testing the function on various inputs
print(count_upper('aBCdEf'))  # Expected output: 1
print(count_upper('abcdefg'))  # Expected output: 0
print(count_upper('dBBE'))  # Expected output: 0
```

This script passes all the tests and provides the correct output based on the given Python script and tests.