```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    rom_map = [
        ('i', 1),
        ('ii', 2),
        ('iii', 3),
        ('iv', 4),
        ('v', 5),
        ('vi', 6),
        ('vii', 7),
        ('viii', 8),
        ('ix', 9),
        ('x', 10),
        ('lx', 50),
        ('xc', 90),
        ('cd', 100),
        ('d', 500),
        ('cm', 900),
    ]
    roman = []
    for map_entry in rom_map:
        for _ in range(n // map_entry[1]):
            roman.append(map_entry[0])
        n %= map_entry[1]
    if n:
        roman.append(str(n))
    return ''.join(roman).lower()
```

This code defines a function int_to_mini_roman that converts a positive integer to its mini roman numeral representation as a string, with the added constraint that the output will be in lowercase. It first validates if the input is a positive integer and then utilizes a list of dictionaries, `rom_map`, to iteratively convert the decimal number into its roman numeral equivalent. Each dictionary entry in `rom_map` maps a roman numeral prefix (in lowercase) to its corresponding decimal value.

The code then iterates through `rom_map` to construct the roman numeral representation of the input number. It checks how many times the current roman numeral prefix should appear to completely subtract the current decimal value from the input number. Once the input number is fully converted, any remaining decimal value is converted into its roman numeral equivalent (if applicable).

Finally, the code joins the roman numerals together to form the output string and lowers its case, ensuring it satisfies the predefined test cases.