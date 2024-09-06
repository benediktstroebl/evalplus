def string_xor(a, b):
    return '\n'.join(x ^ y for x, y in zip(a.strip('0').strip('1'), b.strip('0').strip('1')))