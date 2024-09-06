
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None

    # Convert the input string to bytes.
    bytes_text = bytes(text, 'utf-8')

    # Convert the bytes to a binary string and hash it.
    hash_md5 = hashlib.md5(bytes_text).hexdigest()

    return hash_md5
