def int_to_mini_roman(num):
    if num < 1000:
        # Convert to string and remove any decimal points
        num = str(num)
        roman_values = {
            'i': 1, 'v': 5, 'x': 10,
            'l': 50, 'c': 100, 'd': 500, 'm': 1000
        }
        result = []
        for char in num:
            if char.isalpha():
                result.append(char)
            elif char == '.':
                result.append('0')
            elif char == '-':
                result.append('m')
        roman_num = ''
        for char in result:
            if char in roman_values:
                roman_num += roman_values[char]
            elif char == '0':
                roman_num += 'n'
        return roman_num.lower()
    else:
        return "Invalid number provided"