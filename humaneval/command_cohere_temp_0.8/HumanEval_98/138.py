```python
def count_upper(s):
    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    count = 0
    for i in range(0, len(s), 2):
        if s[i].upper() in upper_vowels:
            count += 1
    return count
```

This script defines a Python function called `count_upper` that solves the problem statement. It counts the number of uppercase vowels in the even indices of a given string `s` and returns the count. The function utilizes a list `upper_vowels` to store all the uppercase vowels, loops through the string checking every second index, and increments the count if an uppercase vowel is encountered.

The provided solution has a time complexity of `O(n/2)` where `n` is the length of the input string, and a space complexity of `O(1)` as it only uses a constant amount of extra space to store the `upper_vowels` list.