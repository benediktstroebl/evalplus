Here's a Python script with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Using list comprehension to check if each character in the string is an uppercase vowel
    uppercase_vowels = [char.upper() for char in s if char.isupper() and char in 'AEIOU']
    # Using list comprehension to check if each even index in the string contains an uppercase vowel
    even_indices = [i for i in range(0, len(s), 2) if s[i] in uppercase_vowels]
    return len(even_indices)
```

This script defines a function `count_upper()` that takes a string as an argument and returns the number of uppercase vowels in even indices of the string. It utilizes the `isupper()` method and the `in` operator to find occurrences of uppercase vowels in the even indices of the string.

To get the result, simply run the script and provide the function the string you want to analyze. 
Here are some examples of test cases to ensure the function behaves correctly:
```python
print(count_upper('aBCdEf'))  # Output: 1
print(count_upper('abcdefg'))  # Output: 0
print(count_upper('dBBE'))  # Output: 0
```

The output should be:
```
1
0
0
```