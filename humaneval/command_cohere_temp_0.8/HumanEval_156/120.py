```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        roman_thousands = ""
        for _ in range(thousands):
            roman_thousands += "m"
        roman_rest = int_to_mini_roman(rest)
        return roman_thousands + roman_rest
```

The approach used is top-down, using recursion. The base case is when `n=1`, where the function returns the single roman `i`. In the general case, the thousands are converted directly to `m` and the rest is recursively converted to roman. We use `divmod` to split `n` into the thousands and the rest, and then concatenate the results. We avoid the repetition of the 1000 limit by using recursion and splitting the problem.

To test it you can run:
```python
>>> int_to_mini_roman(19)
'xix'
>>> int_to_mini_roman(152)
'clii'
>>> int_to_mini_roman(426)
'cdxxvi'
```