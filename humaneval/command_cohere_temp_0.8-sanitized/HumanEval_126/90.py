def is_sorted(lst):
    # Preprocessing
    seen = set()
    duplicates = []
    for num in lst:
        if num in seen:
            duplicates.append(num)
        seen.add(num)
    if len(duplicates) > 1:
        return False

    # Sorting
    lst.sort()
    return lst == list(map(lambda x: x, lst))