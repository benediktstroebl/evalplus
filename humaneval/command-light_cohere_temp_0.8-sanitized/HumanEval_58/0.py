def common(list1: list, list2: list) -> list:
    """Return sorted unique common elements for two lists"""
    set1 = set(list1)
    set2 = set(list2)
    common = set1.interunion(set2)
    return list(common)