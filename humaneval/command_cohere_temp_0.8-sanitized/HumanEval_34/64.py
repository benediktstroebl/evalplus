def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted([item for item in l if not (item in seen or seen.add(item))])