Here's the Python code to solve the problem:
```python
def count_upper(s):
    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This function `count_upper()` takes a string `s` as input and counts the number of uppercase vowels in even indices. It utilizes a list `upper_vowels` containing all uppercase vowels to efficiently check if a character is a vowel and uppercase. The function then iterates through the string at even indices, checking if the character is both uppercase and a vowel, and increments the count if so. The result is the total count of uppercase vowels in even positions in the string. 

Let's verify the behavior with some examples:
```python
print(count_upper('aBCdEf'))  # Output: 1
print(count_upper('abcdefg'))  # Output: 0
print(count_upper('dBBE'))     # Output: 0
```

The output will be as follows:
```bash
1
0
0
``` 

The first example passes since 'A' at index 0 is an uppercase vowel in an even position. In the second, there are no uppercase vowels in even positions. The third example also yields no counts, as 'D' and 'B' are not uppercase vowels in even positions.