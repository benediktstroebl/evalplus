```python
def int_to_mini_roman(num):
    rom_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_dict = {v: k for k, v in enumerate(rom_values)}

    result = []
    while num > 0:
        fraction = num // roman_dict[rom_values[-1]]
        result.append(str(fraction))
        num = num - fraction * roman_dict[rom_values[-1]]
        rom_values.pop()

    reversed_result = ''.join(reversed(result))
    return reversed_result.lower()
```

The logic behind the code:
1. The `rom_values` list stores the roman numerals in descending order, ensuring the correct translation of the largest possible value.
2. The `roman_dict` dictionary creates a reversible mapping from roman numerals to their corresponding integer values, aiding in translating back and forth.
3. The `result` list accumulates the roman numerals as we iterate through the divisors of the input number.
4. By converting the largest value first and working downwards, the code ensures that the roman numerals are translated accurately, delivering the `reversed_result` in the intended format.

With this approach, the code effectively converts integers into roman numerals using the efficient divisor-based method, producing the desired `reversed_result` in the process.