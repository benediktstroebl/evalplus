```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[letters == 'abcdefghijklmnopqrstuvwxyz'].swapcase()
```
This Python script defines a function `solve` that takes a string `s` as input and performs the tasks specified in the problem statement. Here's how the function works:
1. The `letters` string contains all lowercase and uppercase letters, which is used to check if the current character in the string `s` is a letter or not.
2. The `swapcase()` method is used to swap the case of characters in a string. This method doesn't modify the characters that are not letters, which is why we use it to determine which characters to swap the case of and which ones to leave as they are.
3. If the set of characters in the string `s` contains only letters, the `swapcase()` method is called on the string, which will swap the case for all characters, both letters and non-letters.
4. If the string `s` contains non-letter characters, we use a conditional expression to check if the current character is a letter. If it is, we apply the `swapcase()` method to the letter, otherwise, we keep the character as it is. This is done using the `[letters == 'abcdefghijklmnopqrstuvwxyz'].swapcase()` method, which applies the `swapcase()` method only to the characters that are letters (while keeping non-letter characters unchanged).

Overall, this function solves the problem by appropriately reversing the case of letters in a string while leaving non-letter characters unchanged, as specified in the problem statement.