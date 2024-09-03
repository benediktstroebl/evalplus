def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_length = max(len(s) for s in strings)
    return strings[0].center(max_length)