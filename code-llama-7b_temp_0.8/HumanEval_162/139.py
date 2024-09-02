
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    from string import hexdigits

    # Hint:
    # - Use the hashlib module to calculate the md5 hash of 'text'.
    # - Use the str.translate(str.maketrans()) method to replace
    #   non hexdigits (i.e. all the characters that are not in
    #   the hexdigits string) with '' (i.e. nothing).
    # - Then use the join() method to concatenate all the characters
    #   in the list returned from the split() method into a single
    #   string.

    if len(text) == 0:
        return None

    return ''.join(hashlib.md5(text.encode()).hexdigest().translate(str.maketrans('', '', ''.join(hexdigits[:10]))).split())
