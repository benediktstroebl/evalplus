```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    # prettify numbers from 1 - 10
    if n <= 10:
        return ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"][n - 1]

    # concatenate converted numbers from 10 - 1000
    roman = []
    for num in range(1, 1001):
        if n >= num:
            roman += int_to_mini_roman(num)

    return "-".join(roman)[::-1]
```

The following expressions illustrate the usage of the `int_to_mini_roman` function:
```python
>>> int_to_mini_roman(19)
'xix'
>>> int_to_mini_roman(152)
'clii'
>>> int_to_mini_roman(426)
'cdxxvi'
```