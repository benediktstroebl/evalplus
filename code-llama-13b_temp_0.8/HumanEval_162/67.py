
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # Representing md5 hash as 128-bit binary number
    binary_string = text.encode('utf-8')
    m = hashlib.md5()
    m.update(binary_string)
    digest = m.digest()
    binary_md5 = bin(int.from_bytes(digest, 'big'))
    return binary_md5

