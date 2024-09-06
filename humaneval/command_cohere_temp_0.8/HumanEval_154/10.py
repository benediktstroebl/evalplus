```python
def cycpattern_check(a, b):
    a, b = a.lower(), b.lower()
    return any(b in s for s in a) or any(a == s for s in rotate(a))

def rotate(s):
    return s[:i] + s[i+1:] for i in range(len(s))
``` 

The `cycpattern_check` function takes two strings as input and returns a boolean indicating whether the second word or any of its rotations is a substring in the first word. The `rotate` function creates all possible rotations of the first string and returns them. This function utilizes lowercase conversion and uses string methods to efficiently check for substring occurrences.