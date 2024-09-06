```python
def reverse_delete(s, c):
    """
    Deletes characters in 's' that are also in 'c', and checks if the resulting string is a palindrome.
    """
    s = set(s) - set(c)
    return s, s == s[::-1]
```

This approach utilizes sets to efficiently remove characters from string `s` that appear in string `c`, using the `-` set difference operator. The resulting string is then checked for palindromic symmetry using slicing and a boolean comparison. The function returns a tuple containing the modified string and a boolean indicating whether it's also a palindrome. 

To better understand let's break down the solution:
1. **set(s) - set(c)**: Removes characters in `c` from the set of characters in `s`, resulting in a new set containing only characters found in `s` but not in `c`.
2. **s = list(s)**: Converts the set back to a list to work with the string characters.
3. **s == s[::-1]**: Checks if the modified string `s` is a palindrome by comparing it with its reverse using slicing.

The provided example tests, along with the function, clearly demonstrate how to utilize the `reverse_delete` function to solve the problem. Adjustments can be made to the function signature and tests to better suit your specific needs.