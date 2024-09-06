import math
def hex_key(num):
    prime_hex = [int(d) for d in '0123456789ABCDEF' if d in '23579B' or d in '13579D']
    return sum(1 for d in num if d in prime_hex)