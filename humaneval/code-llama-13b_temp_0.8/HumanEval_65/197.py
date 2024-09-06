
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    """
    cara yang pertama yaitu fungsi terpisahkan, kita pisahkan angka2nya, lalu angkanya dikurangi angka shift, 
    lalu dibagi angka x, kemudian diubah menjadi string, lalu diubah kembali menjadi int.
    """
    x = str(x)
    return int(str(x[-shift:] + x[:-shift]))

    # or
    # ...
    # return int(''.join(str(x)[-shift:] + str(x)[:-shift]))

