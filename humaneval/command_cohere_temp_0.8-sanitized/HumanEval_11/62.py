def string_xor(a, b):
    return a.translate(str.maketrans('01','10')) == b.translate(str.maketrans('10','01'))