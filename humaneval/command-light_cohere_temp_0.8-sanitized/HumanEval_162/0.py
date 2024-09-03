import hashlib
def string_to_md5(text):
    if not text:  # empty string returns None
        return None
    return hashlib.md5arenum(text)