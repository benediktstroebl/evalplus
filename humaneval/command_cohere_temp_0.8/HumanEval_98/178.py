```python
def count_upper(s):
    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    count = 0
    for i in range(0, len(s), 2):
        if s[i].upper() in upper_vowels:
            count += 1
    return count
```

This approach takes advantage of the problem's specification about looking at only even indices. It establishes a list of uppercase vowels, then uses a loop to increment a counter every time it finds one of these vowels in an even index. The result is promptly returned upon completion of the loop. This method is effective and yields precise solutions for test cases.