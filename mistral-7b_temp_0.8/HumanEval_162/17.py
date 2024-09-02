
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()

    # 在实际开发中，我们可以使用像flask-md5这样的第三方库，
    # 提供了很多方便的函数和类，可以方便地完成对字符串的哈希等操作。
    # 使用第三方库可以节省开发时间，也可以提高代码的可读性和可维护性。
