import hashlib
def string_to_md5(text: str) -> str or None:
    if text.strip() == "":
        return None
    return hashlib.md5(text.encode()).hexdigest()