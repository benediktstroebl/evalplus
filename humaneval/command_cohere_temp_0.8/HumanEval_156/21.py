```python
def int_to_mini_roman(n):
    if n < 1:
        return ""
    
    mini_roman = [
        'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x',
        'l', 'lx', 'lxx', 'lxxx', 'xc', 'xcix', 'cc', 'ccc', 'cd', 'cdi', 'cdii',
        'd', 'dx', 'dxii', 'dxiii', 'dvi', 'dvii', 'dxv', 'dxvi', 'dxvii', 'dxviii', 'dxix',
        'm', 'mx', 'mxx', 'mxxx', 'cm', 'cmx', 'cmxx', 'cmxxx'
    ]

    rom_num = [0] * (n + 1)
    rom_num[0] = mini_roman[0]
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            if rom_num[j] != '':
                break
        if i != j:
            rom_num[i] = mini_roman[i] + rom_num[j]
        else:
            rom_num[i] = mini_roman[i]

    result = ""
    for char in rom_num:
        result += char
    return result.lower()
```

This approach uses a list `rom_num` to store the roman numerals starting from `i` up to the number to be converted. It then sequentially fills the list with the appropriate roman numerals based on their decimal equivalents. Finally, the function returns the content of `rom_num` as a roman numeral string, ensuring it is lowercase.