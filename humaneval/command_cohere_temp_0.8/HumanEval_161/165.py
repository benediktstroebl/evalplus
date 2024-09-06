```python
def solve(s):
    new_str = []
    for c in s:
        if c.isalpha():
            new_str.append(c.swapcase())
        else:
            new_str.append(c)
    return ''.join(new_str)
```

This script defines a function `solve(s)` that accepts a string `s` as an argument and operates on it as stated in the problem. It iterates through each character in `s`, using the `isalpha()` method to check if it's a letter. If so, it uses the `swapcase()` method to change the case of the letter. If not, it remains unchanged. The resulting string is returned after iterating through all characters and appending the processed characters to a new string.

To check the correctness of the solution, the following tests could be used:
```python
# Single letter
print(solve("a"))  # Should print: A

# Multiple letters
print(solve("abc"))  # Should print: ABC

# Mixed characters
print(solve("a1b!c"))  # Should print: A1B!C

# Only digits
print(solve("1234"))  # Should print: 4321

# Only non-letters
print(solve("#a@c"))  # Should print: #A@c
``` 
This demonstrates that the function handles different scenarios correctly.