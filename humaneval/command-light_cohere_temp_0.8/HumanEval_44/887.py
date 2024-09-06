```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers use 10 or either the string representation of a number using a given base.
    >>> change_base(8, 3)
    '22'
    >>> change_base(5, 16)
    '8'
    >>> change_base(123, 2)
    '1111'
    >>> change_base(7, 5)
    '111'
    >>> change_base(1, 1000)
    Traceback (most recent call last):
      File "<stdin>", line 19, in <module>
    ValueError: invalid literal for int() with base 10: '111'
    """
    # Perform the conversion
    if x < 0:
        x = (-x)
    temp = bin(x)[2:]
    i = 0
    while i < len(temp):
        if temp[i] == '1':
            break
        i += 1
    while i < len(temp):
        if temp[i] == '0':
            i += 1
        else:
            break
        j = i
        while j < len(temp) and temp[j] == '1':
            j += 1
        s = temp[i:j] + temp[j+1:]
        i = j
        temp = temp[:i] + '0' + temp[j+1:]
    return s
```  This code defines a function `change_base` that takes an integer `x` and an integer `base` as input and returns the converted string representation of `x` in the given `base`. It uses a loop to convert the number into the desired base, then returns the string.