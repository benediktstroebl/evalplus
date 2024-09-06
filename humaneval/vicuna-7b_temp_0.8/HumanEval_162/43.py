
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None

    # Convert text to bytes
    bytes_text = bytes(text, 'utf-8')

    # Create a new md5 hash object
    hash_md5 = hashlib.md5()

    # Update the hash with the bytes_text
    hash_md5.update(bytes_text)

    # Calculate the hex digest of the hash
    digest = hash_md5.hexdigest()

    return digest
