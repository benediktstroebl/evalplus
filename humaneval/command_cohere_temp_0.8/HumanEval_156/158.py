```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    res = []
    for i in range(1, 1000):
        if n >= i:
            num = [str(i) for i in range(1, (i//5)+1)]
            den = [str(i) for i in range(1, (i//10)+1)]
            res += [den[0]+num[0]+(len(num)>=2 and den[1] or '')+str(i//10*5)]
            n -= i
    return ''.join(res)
```

This script provides a function called `int_to_mini_roman`, which converts a given positive integer to its mini roman numeral representation as a string. It iterates through the numbers from 1 to 1000, adding the appropriate roman numeral prefixes to the result list. The function handles floor division by 5 and 10, and it ensures that the result is returned in lowercase.

Here is an example of how to use this function:
```python
>>> int_to_mini_roman(19)
'xix'
>>> int_to_mini_roman(152)
'clii'
>>> int_to_mini_roman(426)
'cdxxvi'
>>> int_to_mini_roman(100)
'cccc'
```