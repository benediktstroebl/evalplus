```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if len(s) == len(set(s)) else s[::-1]
```
This Python script defines a function `solve` that takes a string `s` as input and performs the following steps to solve the specified problem:

It checks if any character in the string is a letter by looking for characters in the `letters` string, which contains all uppercase and lowercase letters. This is done using the `len(set(s))` argument which counts the unique characters in the string. If the string has the same length as the number of unique characters (i.e., there are no letters), it means the string is made up of non-letter characters only. In this case, the function calls `s.swapcase()` to reverse the string. The `swapcase()` method swaps the case of each character in a string. 

If the string does contain letters, the function calls `s.swapcase()` to toggle the case of each letter character in the string. This results in shifting uppercase letters to lowercase and vice versa. 

The function returns the resulting string from either the `swapcase()` or the reverse operation.

This solution is concise and maintains the letter case as described in the problem statement.