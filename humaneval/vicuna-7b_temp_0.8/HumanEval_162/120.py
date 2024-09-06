
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None

    # Convert the input string to bytes
    text_bytes = bytes(text, 'utf-8')

    # Create a new md5 hash object
    md5_hash = hashlib.md5()

    # Update the hash with the bytes
    md5_hash.update(text_bytes)

    # Get the hash value as a bytes object
    return bytes(md5_hash.digest())
