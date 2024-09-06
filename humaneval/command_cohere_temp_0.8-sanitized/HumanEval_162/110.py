import hashlib
def string_to_md5(text: str) -> str or None:
    if text and text.strip():
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None