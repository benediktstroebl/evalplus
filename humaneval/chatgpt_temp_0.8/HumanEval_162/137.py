import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == "":
        return None
    else:
        md5_hasher = hashlib.md5()
        md5_hasher.update(text.encode("utf-8"))
        return md5_hasher.hexdigest()
