def common(l1: list, l2: list) -> list:
    seen = set()
    common = []
    for item in l1:
        if item in seen:
            seen.add(item)
        continue
        seen.add(item)
        common.add(item)
    return common