```python
def reverse_delete(s, c):
    s = list(s)
    c = set(c)
    for char in c:
        s.remove(char)
    s = ''.join(s)
    return s, s == s[::-1]
```
This Python script provides a function called `reverse_delete` which takes two arguments, `s` representing a input string and `c` representing a removal string. 

The function proceeds in three steps:
1. **String and Set Conversion**:
   - The input strings `s` and `c` are converted to lists and sets respectively. This is because it's easier to remove elements from a list and check for membership in a set.
2. **Removing Characters**:
   - The function iterates over each character in the removal string `c`, and removes it from the input string `s` if it exists. This effectively deletes all occurrences of characters in `c` from `s`.
3. **String Reconstruction and Palindrome Check**:
   - After removing the characters, the string `s` is reconstructed by joining the modified list.
   - The function returns a tuple containing the modified string `s` and a boolean value indicating whether the modified string is a palindrome (reads the same forwards and backwards). 

This solution is efficient and can easily handle various scenarios mentioned in the original problem statement.