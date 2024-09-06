Here's a Python script with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices. The function first creates a set of uppercase vowels to simplify the lookup process. It then iterates through the characters of the input string in pairs, checking if the character at even indices is an uppercase vowel. The result is returned as the count of uppercase vowels in even indices. 

The example tests provided in the initial prompt return the following results:
```python
print(count_upper('aBCdEf')) # 1
print(count_upper('abcdefg')) # 0
print(count_upper('dBBE')) # 0
``` 

This demonstrates the correctness of the function. Feel free to modify the tests or ask for additional assistance as needed.