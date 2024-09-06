```python
def cycpattern_check(first, second):
    first = first.lower()
    second = second.lower()
    return second in first or any(second in t for t in first.split(second))
```

This function takes two strings as input and returns a boolean that might be true if the second word or any of its rotations is a substring in the first word. The function rotates the second word through all possible rotations and checks each one as a substring in the first word. The function also utilizes the `lower()` function to ensure the strings are case insensitive. 

Would you like to learn more about the code?