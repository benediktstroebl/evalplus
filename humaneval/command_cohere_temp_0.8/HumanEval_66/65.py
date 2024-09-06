```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```

The function `digitSum` leverages Python's built-in function `sum` along with a list comprehension that traverses each character in the string `s`. The comprehension filters character entities that have uppercase letters with `c.isupper()`, acquiring their numerical value through `ord(c)`, which evaluates the character to a unique integer representing its ASCII code. These sums are then aggregated by the `sum` function and returned as the function output.

This method is both effective and concise, producing a sum of the upper characters exclusively from the input string.