
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    import hashlib

    # In order to avoid naming conflicts with the module-level variable of the same name,
    # this function should use a different name for its local variable.
    # Also, it should use the module-level variable as a method of the hashlib module.
    # Furthermore, a 2-tuple of arguments for the method should be passed.
    # Use a "list comprehension" to construct the argument list.
    # Your function should return a string.
    return hashlib.md5([text]).hexdigest()

