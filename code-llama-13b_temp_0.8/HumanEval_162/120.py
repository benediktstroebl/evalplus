
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    # Create an empty string to store the return value.
    return_value = ''

    # If 'text' is an empty string, return None.
    if not text:
        return None

    # Import the hashlib module if necessary.
    import hashlib

    # Create an MD5 hash object.
    m = hashlib.md5()

    # Update the hash with the text's bytes.
    m.update(text.encode('utf-8'))

    # The resulting md5 hash is stored in return_value.
    return_value = m.hexdigest()

    # Return the md5 hash equivalent string.
    return return_value
