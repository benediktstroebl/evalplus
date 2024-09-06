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

This script defines a function `count_upper()` which takes a string as an argument and returns the number of uppercase vowels in even indices of that string. The function first creates a set of uppercase vowels and initializes a counter to 0. It then iterates through the string, checking if each character is an uppercase vowel and if it is in an even index. If both are true, the counter is incremented. The function finally returns the counter's value. 

The tests for this function create examples where the number of uppercase vowels in even indices is either 1, 0, or none, testing the function's correctness.