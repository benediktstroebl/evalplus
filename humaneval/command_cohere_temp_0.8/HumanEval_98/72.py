Here's a Python script that contains a function named `count_upper()` which solves the problem as described in the markdown code block:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    vowels = 'AEIOU'
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This function takes a string s as input and counts the number of uppercase vowels in even indices. It does so by first creating a boolean variable named count and initializing it as 0, and a string variable named vowels containing the uppercase vowels 'AEIOU'. It then loops through the characters in s in increments of 2, checking if the character is uppercase and within the vowels string, and finally returns the count variable.

Here's a simplified test case to demonstrate the functionality of the function:
```python
print(count_upper('aBCdEf')) # Output: 1
```
This will return 1, since the uppercase vowel 'E' is in an even index.

Here's another test case to further demonstrate its range:
```python
print(count_upper('abcdefg')) # Output: 0
print(count_upper('dBBE')) # Output: 0
```
The function will return 0 in these cases, as there are no uppercase vowels in even indices.