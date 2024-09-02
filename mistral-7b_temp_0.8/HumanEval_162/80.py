
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # Replace this for loop with a while loop.
    # The hashlib.md5 method takes in a string, and returns a string.
    # print(hashlib.md5(text).hexdigest())
    result = ""
    for i in range(len(text)):
        result += hashlib.md5(text[i]).hexdigest()
    return result

