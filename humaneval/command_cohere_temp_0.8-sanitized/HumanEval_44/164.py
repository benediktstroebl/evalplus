def change_base(x, base):
    return str(x).translate(str.maketrans('1234567890', f'{base}_{base}_{base}_{base}'))