
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # initialize the md5 hash object
    import hashlib
    hash_object = hashlib.md5()

    # update the hash_object with the text
    hash_object.update(text.encode())

    # return the result as a string
    return hash_object.hexdigest()

