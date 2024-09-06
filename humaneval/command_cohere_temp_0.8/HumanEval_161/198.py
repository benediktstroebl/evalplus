```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) else s[::-1]
```
This Python script defines a function `solve` taking one argument `s` which performs the desired operations as described in the prompt that includes checking if the string contains letters or not. The `swapcase` method is used if there are letters in the string, which reverses the case of letters while leaving non-letter characters unchanged. If the string contains no letters, it is reversed using slicing notation `[::-1]`. This approach ensures that the function remains self-contained without importing any additional libraries.