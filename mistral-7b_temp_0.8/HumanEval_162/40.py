
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # return hashlib.md5(text.encode()).hexdigest()

    # d = hashlib.md5()
    # d.update(text.encode())
    # return d.hexdigest()

    # m = hashlib.md5()
    # m.update(text.encode())
    # return m.hexdigest()

    # hash_md5 = hashlib.md5(text.encode('utf-8'))
    # return hash_md5.hexdigest()

    # md5 = hashlib.md5()
    # md5.update(text.encode('utf-8'))
    # return md5.hexdigest()

    # m = hashlib.md5()
    # m.update(text.encode('utf-8'))
    # return m.hexdigest()

    # d = hashlib.md5()
    # d.update(text.encode())
    # return d.hexdigest()

    # m = hashlib.md5()
    # m.update(text.encode('utf-8'))
