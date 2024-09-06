def strange_sort_list(lst):
    # Create a copy of the list to avoid original modification
    result = lst.copy()
    result.sort(key=lambda x: [x in result[:-1], x in result[-1:]].index(True))
    return result