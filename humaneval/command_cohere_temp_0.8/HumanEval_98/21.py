Here's the Python code with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    Example:
    >>> count_upper('aBCdEf')
    1
    >>> count_upper('abcdefg')
    0
    >>> count_upper('dBBE')
    0
    """
    # Use a dictionary to store the count of each vowel
    vowel_count = { 'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0 }
    # Iterate through the string
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper():
            if s[i] in vowel_count:
                vowel_count[s[i]] += 1
    # Sum the counts and return the result
    return sum(vowel_count.values())
```
This function uses a dictionary to keep track of the count of each uppercase vowel it encounters in the even indices of the string. Finally, it returns the sum of these counts, which gives the number of uppercase vowels in even indices. 

The example usage outputs 1 for 'aBCdEf', 0 for 'abcdefg', and 0 for 'dBBE', as given in the prompt.