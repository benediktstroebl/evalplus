def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123'))