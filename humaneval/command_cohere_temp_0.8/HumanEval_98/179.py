Here's a Python script that contains a function to solve the problem you've described:
```python
def count_upper(s):
    upper_vowels = "AEIOU"
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This function `count_upper` takes a string `s` as input and counts the number of uppercase vowels in even indices. It uses a generator expression along with the `isupper` and `in` functions to check if each character in even indices is an uppercase vowel.

The example inputs provided in the original prompt return the following results:
- `count_upper('aBCdEf')` returns 1 
- `count_upper('abcdefg')` returns 0
- `count_upper('dBBE') returns 0` 

These results are consistent with the problem statement. 

If you have additional requirements or more complex scenarios, feel free to provide them, and I'll adapt the code to handle them accordingly.