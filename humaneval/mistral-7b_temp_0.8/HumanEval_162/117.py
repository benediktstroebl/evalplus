
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    from hashlib import md5
    from string import Template
    tpl = Template("$s")

    def my_md5(s):
        return md5(tpl.substitute(s=s).encode()).hexdigest()

    return my_md5(text)
