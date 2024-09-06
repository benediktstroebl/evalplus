def change_base(x, base):
    return str(x).encode('utf-8')[::base].decode('utf-8')