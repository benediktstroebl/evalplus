```python
def count_upper(s):
    cnt = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in 'AEIOU':
            cnt += 1
    return cnt
```

This function `count_upper()` takes a single argument `s`, which is the string for which we want to count the number of uppercase vowels in even indices. The function then iterates through the string at intervals of two indices using the `for` loop with the `range(0, len(s), 2)` argument. When it iterates through these two-indexed indices, it checks if the character is uppercase (`s[i].isupper()`), and if it's an uppercase vowel (`s[i] in 'AEIOU'`). If both conditions are met, it adds 1 to the `cnt` variable. Finally, the function returns the `cnt` variable as the number of uppercase vowels in even indices.

Here is a simple test drive function to test the above function:
```python
def test_count_upper():
    assert count_upper('aBCdEf') == 1
    assert count_upper('abcdefg') == 0
    assert count_upper('dBBE') == 0
```