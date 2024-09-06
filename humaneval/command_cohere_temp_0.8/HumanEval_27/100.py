```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c.swapcase() if c.isupper() else c for c in string)
```

This code uses a list comprehension with conditions based on the character's case to determine whether to use `swapcase` or not. This ensures that the behavior of keeping non-alphabetic characters and lowercase letters unchanged is maintained.

To better understand the list comprehension, let's break it down step by step:
1. **Initialization of Empty List**: `return ''.join()` initializes an empty list to accumulate the modified characters.
2. **Iterating Over String Characters**: The `for c in string` loop iterates through each character of the input `string`.
3. **Conditional Swapping**: The conditions `if c.islower():` and `if c.isupper():` check if the character (`c`) is in lowercase or uppercase, respectively. If the condition is true, the `swapcase()` function is applied to the character, otherwise, the character remains as is.
4. **Appending to List**: The result of the conditions is appended to the empty list with `c` or `c.swapcase()`).
5. **Joining the List into a String**: Once all characters are processed, the list is joined into a single string again using the `join()` method.

This should provide a clear understanding of how the list comprehension works and why it leads to the desired behavior. Let me know if you need further clarification on any specific part!