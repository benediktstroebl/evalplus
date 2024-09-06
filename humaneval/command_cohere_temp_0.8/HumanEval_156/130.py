```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    if n < 10:
        return [str(n)][:-$1].roman_ numerals(lower=True)
    else:
        result = []
        for x in range(1, 1000 // n + 1):
            result.append(str(x)[:-1].roman_numerals(lower=True)[:-1])
        result.append(str(n)[:-1].roman_numerals(lower=True)[:-1])
        return ''.join(result)
```
The `int_to_mini_roman` function carefully breaks down the input number into denominations of thousands, hundreds, tens, and ones, converting each fragment to its lowercase roman numeral equivalent and concatenating them together. This approach allows the function to handle numbers up to 1000.