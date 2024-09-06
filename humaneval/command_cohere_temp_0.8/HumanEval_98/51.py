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
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` which takes a string `s` as input and counts the number of uppercase vowels in even indices. The function uses a list to store the uppercase vowels ('AEIOU') and iterates through the input string in increments of 2, checking for uppercase vowels in each even index. Every count is added to the total until all even indices have been checked. Ultimately, the function returns the total count of uppercase vowels in even indices. 

The expected output for the provided examples is:
```
1
0
0
```