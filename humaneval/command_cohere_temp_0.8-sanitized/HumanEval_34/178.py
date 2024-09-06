def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted(seen.add(x) for x in l if x not in seen and x != '')