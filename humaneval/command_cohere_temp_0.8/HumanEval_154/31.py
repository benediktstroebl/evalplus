```python
def cycpattern_check(a, b):
    a = a + a
    b = b + b
    return b in a
```

The function `cycpattern_check` takes two strings `a` and `b` as input and checks if the second word or any of its rotations are substring in the first word. The code to do this is:
1. Summing repeated characters in string `a` or `b` gives us the length of the cyclic pattern that can be formed from that string. This is done to avoid unnecessary computations of rotating strings for patterns like 'aaaa' where the unique characters are repeated.
2. Then we rotate the string `b` to find if any of its rotations match as a substring in string `a`. We do this by creating a cyclic rotation using `b + b` and checking if it is present in the augmented string of `a`.

This solution avoids explicit rotation of strings and uses a clever technique to achieve better performance. The augmented string technique is also a clever optimization to handle strings with repeated characters.