```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[letters::letters]
```
This Python script defines a function `solve` that takes a string `s` as input and performs the tasks specified in the problem statement. 

The function first checks if the string contains any letters, and if not, it simply reverses the string using the `swapcase` method, as there are no letter characters to manipulate. This behavior is specified in the `solve` function's second paragraph ("If the string contains no letters...").

If the input string `s` does contain letter characters, the function utilizes the `swapcase` method to selectively reverse the case of each letter while keeping non-letter characters unchanged. This is achieved by using the string `letters` to create a letter-indexed string slice. This `letters` string contains all possible letter characters, both in lower and upper case, thus serving as an indexable template for switching letter cases. The `s.swapcase()[letters::letters]` expression achieves the desired case flipping of letters while keeping non-letter characters unchanged.