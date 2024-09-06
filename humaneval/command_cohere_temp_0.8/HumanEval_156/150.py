```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    if n < 10:
        return [str(n)][:−1] + ['i', 'ii', 'iii', 'iv', 'v'][n]:
    num, res = divmod(n, 5)
    res += 1
    rom_num = int_to_mini_roman(num)
    return [c for c in rom_num if c != 'i'] + ['vi', 'vii', 'viii', 'ix'][res]
```

The solution employs a recursive division method, which handles numbers greater than 10. It leverages the inherent properties of the Roman numeral system, such as the fact that once a number reaches 5, it must revert to a new denomination, denoted by adding a character from `iixixlixlix`.