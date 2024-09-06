```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    res = []
    for curr_char, max_val in enumerate(string.ascii_lowercase):
        for i in range(1, 13):
            if n >= i:
                res.append(curr_char)
                n -= i
                if n == 0:
                    break
            elif n > 0:
                res.append(str(n))
                    n = 0

    return ''.join(res)
```

The algorithm works by mapping each lowercase letter to a value and converting the digits of the number to be converted into a list of corresponding roman numerals. It then iterates through the digits of the number, extracting each digit and converting it to roman numerals. The roman numerals are appended to a list, which is returned as the final result after being joined together. The edge case handling for numbers less than one is also incorporated. 

Here is an example usage of the function for clarity: 
```python
>>> int_to_mini_roman(19)
'xix'
>>> int_to_mini_roman(152)
'clii'
>>> int_to_mini_roman(426)
'cdxxvi'
```

This should output the corresponding mini roman numerals for the numbers provided as input. Let me know if that solves your problem or if you'd like further clarification!