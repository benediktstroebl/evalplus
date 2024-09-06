```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        if thousands:
            return "{}m".format(thousands)
        dozens, rest = divmod(rest, 100)
        if dozens:
            return "{}x".format(dozens)
        tens, units = divmod(rest, 10)
        if tens:
            return "{}{}".format(int_to_mini_roman(tens), "i")
        if units:
            return "{}{}".format(int_to_mini_roman(units), "i")
        else:
            return ""
```

The aforementioned code leverages Python's [string concatenation and interpolation](https://docs.python.org/3/reference/expressions.html#string-interpolation) to create the Roman numeral equivalents in a concise manner. Notably, the [divmod()](https://docs.python.org/3/library/functions.html#divmod) function is used to efficiently divide the input into thousands, dozens, and units, with the remainder often representing the tens and units in a more optimized manner. 

To test the function, simply call it with any number between 1 and 1000 and compare the output with the desired Roman numeral.