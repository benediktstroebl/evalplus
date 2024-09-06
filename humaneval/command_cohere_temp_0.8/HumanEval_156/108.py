```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, hundreds, tens, remainder = divmod(n, 1000)
        if thousands:
            return ""
        rom_hundreds = []
        for x in range(hundreds):
            rom_hundreds.append("c")
        rom_ten = ""
        if tens:
            for x in range(tens):
                rom_ten += "x"
        rom_rem = []
        for x in range(remainder):
            rom_rem.append("i")
        roman = rom_hundreds + rom_ten + rom_rem
        roman = "".join(roman).lower()
        return roman
```
The overall approach involves dividing the input number into thousands, hundreds, tens, and remainder (which is less than or equal to 4). The Thousands are handled by checking if thousands are present; if yes, return an empty string. The hundreds are converted directly to romans as a list 'cc', 'xc', 'lc', 'cc', etc.. The tens are converted to roman by iterating and adding appropriate char `x` ('xx', 'xxx', 'xxxx', etc.). The remainder is converted to roman as a list 'i', 'ii', 'iii', 'iv', etc.. Finally, the roman representation is concatenated together and returned.