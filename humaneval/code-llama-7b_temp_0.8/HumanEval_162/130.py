
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    import string
    if text == "":
        return None
    else:
        text_without_spaces = text.replace(" ", "")
        return hashlib.md5(text_without_spaces.encode()).hexdigest()

