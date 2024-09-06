
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # create md5 object from the hashlib library
    md5obj = hashlib.md5()

    # update the md5 object with our input string
    md5obj.update(text.encode())

    # return the hexadecimal equivalent of the md5
    return md5obj.hexdigest()

