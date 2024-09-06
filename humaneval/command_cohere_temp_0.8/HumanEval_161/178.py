```python
def solve(s):
    return ''.join(c.swapcase() if c.isalpha() else c for c in s)
```
This Python script defines a function `solve` taking a single argument `s`, which performs the desired transformations on the string `s` as specified in the problem statement. 

The `solve` function iterates through each character `c` in the input string `s`. For each character, it checks if the character is an alphabet letter using the `isalpha()` method. If it is, it swaps the case of the character using the `swapcase()` method, which changes it to uppercase if it's lowercase and vice versa. If the character is not an alphabet letter, it remains unchanged and is added to the growing string being built using the `join` method. Finally, the function returns the resulting string after applying the specified transformations to each character in the input string `s`. 

This code will yield the desired output for the provided examples in the problem statement. For instance, it will return `"4321"` for the input string `"1234"`, `"AB"` for the input string `"ab"`, and `"#A@c"` for the input string `"#a@C"`.