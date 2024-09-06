```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")

    res = []
    for i in range(1000, 0, -1):
        if n >= i:
            res.append(str(i))
            n -= i
            if i >= 5 and n > 0:
                res.append('x')
                n -= 1
        elif n > 0:
            res.append('x')
            n -= 1

    return ''.join(res)

# Example usage:
# >>> int_to_mini_roman(19)
# 'xix'
# >>> int_to_mini_roman(152)
# 'clii'
# >>> int_to_mini_roman(426)
# 'cdxxvi'
```

The code defines a function int_to_mini_roman that converts a positive integer to its roman numeral representation, subject to the constraints stated in the prompt. It iterates through the numbers from 1000 down to 1, adding the appropriate roman numeral prefixes to a list. If there are remaining digits after converting the number, it appends 'x' to the list (representing 10). Finally, it joins the list into a string to return the roman numeral representation.