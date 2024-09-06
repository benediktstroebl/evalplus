import hashlib
def string_to_md5(text: str) -> str or None:
    if text and text.strip():
        hash_object = hashlib.md5(text.encode())
        return hash_object.hexdigest()
    else:
        return None