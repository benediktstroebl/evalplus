
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    # A list of valid hex decimals.
    hex_digits = ['a', 'b', 'c', 'd', 'e', 'f']

    def to_hex(num):
        """
        Convert an integer to a hexadecimal digit.
        """

        # For an integer 'n', if n <= 9, its hexadecimal representation is
        # n. Otherwise, its hexadecimal representation is
        # 10 + (n % 10)

        if num <= 9:
            return str(num)
        return str(num - 10 + hex_digits.index(hex(num)[-1]))

    # Return None if the string is empty.
    if text == '':
        return None

    md5_hash_value = 0
    for char in text:
        md5_hash_value += ord(char)

    md5_hash_value = str(md5_hash_value)
    md5_hash_value = md5_hash_value[:len(md5_hash_value) // 2]
    md5_hash_value = md5_hash_value[:3] + md5_hash_value[-3:]
    md5_hash_value = int(md5_hash_value)

    return ''.join(map(to_hex, [md5_hash_value]))

