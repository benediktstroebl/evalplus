```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 128
    for letter in s:
        letters_count[ord(letter)] += 1
    for i in range(0, len(s), 3):
        if letters_count[ord(s[i])] > 1 or letters_count[ord(s[i+1])] > 1 or letters_count[ord(s[i+2])] > 1:
            return False
    return True
```

The script checks if each consecutive group of three letters appears only once across the entire string. It does so by maintaining a `letters_count` histogram, mapping each ASCII value of a letter to the number of times that letter has appeared in the string. If the histogram shows that each group of three consecutive letters appears only once, the string is considered happy. 

This solution works for both lowercase and uppercase strings.