```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 256
    for letter in s:
        letters_count[ord(letter)] += 1
    letters_count = [val for val in letters_count if val > 0]
    return len(set(letters_count)) == len(letters_count) == len(s) - 2
```

The script uses an elegant and efficient approach. It first counts the occurrences of each character in the string and then checks whether the counts form a consistent sequence, which is achieved by checking that the unique counts are equal to the total counts which are in turn equal to the length of the string minus 2.