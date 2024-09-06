```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        rom_thousands = chr(ord("m") + thousands)
        rom_rest = int_to_mini_roman(rest)
        return f"{rom_thousands}{rom_rest}"
```

The thousand digits are directly computed by adding the appropriate value to the base 'm' character. A loop isn't required because Python's character indexing is zero-based. The thousands are then joined with the roman representation of the remaining digits (which are handled by recursion) to produce the final roman numeral representation.  This solution is concise and efficient, achieving a time complexity of O(log(N)) thanks to the recursive breakdown.