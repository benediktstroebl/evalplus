```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[letters == 'abcdefghijklmnopqrstuvwxyz'].swapcase()
```
This Python script defines a function `solve` that takes a string `s` as input and performs the tasks specified in the problem statement. Here's how it works:

1. The `solve` function evaluates whether the string contains any letters, by checking if the set of characters in the string `s` has any common elements with the set of lowercase and uppercase letters (`abcdefghijklmnopqrstuvwxyz` and `ABCDEFGHIJKLMNOPQRSTUVWXYZ`).
2. If the string does not contain any letters, it means that all characters are to be reversed. In this case, the function calls the `swapcase()` method on the string `s`, which swaps the case of characters while leaving non-alphabetical characters unchanged. This is a built-in method in Python 2 and 3.
3. If the string contains at least one letter, the function identifies the subset of non-letter characters, by checking which characters from the set of letters are present in the string. 
 4. Then it performs a two-step process: it calls `swapcase()` on the entire string `s`, which will invert the case of all letters. Then it selects the original letters back from the string using the condition `letters == 'abcdefghijklmnopqrstuvwxyz'` which will return a string with all letters in their original case while non-letter characters will be in their swapped case.
 5. Finally, it performs another `swapcase()` on the string with only the original letters, effectively reversing the case of those letters while leaving non-letter characters unchanged.