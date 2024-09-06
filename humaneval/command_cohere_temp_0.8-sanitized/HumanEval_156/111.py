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