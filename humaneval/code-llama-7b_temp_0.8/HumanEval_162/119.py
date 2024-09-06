
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    # Initializing variable to store the md5 hash
    hash = ""

    # If the string is empty return None
    if text == "":
        return None

    # Else calculate the md5 hash of the string and return
    else:
        hash = hashlib.md5(text.encode()).hexdigest()
        return hash

