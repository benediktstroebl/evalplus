```python
def cycpattern_check(first, second):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    first = first.lower()
    second = second.lower()
    rotations = [second, second[1:] + second[:1], second[2:] + second[:2], second[3:] + second[:3]]
    return any(rotations) in first
```

The function `cycpattern_check()` takes two words as input and returns a boolean indicating whether the second word or any of its rotations is a substring in the first word. The function utilizes a list of rotated versions of the second word and uses the any() function to check if any of these rotated versions are substrings of the first word. 

This approach ensures that each rotation of the second word is examined without repeated iterations, resulting in a efficient and concise solution.