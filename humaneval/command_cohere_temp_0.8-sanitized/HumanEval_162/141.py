import hashlib
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to MD5 and returns the hexadecimal representation of the hash.
    Returns None if the input is an empty string.
    """
    if text and text != "":
        md5 = hashlib.md5()
        md5.update(text.encode('utf-8'))
        return md5.hexdigest()
    else:
        return None