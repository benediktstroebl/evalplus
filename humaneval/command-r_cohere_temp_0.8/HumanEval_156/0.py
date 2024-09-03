```python
def int_to_mini_roman(number):
    """
    Converts a positive integer to a lowercase mini Roman numeral.

    Restrictions: 1 <= num <= 1000

    Parameters:
    number (int): The positive integer to convert.

    Returns:
    str: Roman numeral string.
    """
    rom_val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom_sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = ''
    i = 0
    while number > 0:
        for _ in range(number // rom_val[i]):
            result += rom_sym[i]
            number -= rom_val[i]
        i += 1
    return result
```