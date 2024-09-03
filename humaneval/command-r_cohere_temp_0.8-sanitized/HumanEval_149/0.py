def sorted_list_sum(lst):
    result = []
    for word in lst:
        if len(word) % 2 == 0:
            result.append(word)
    result.sort(key=lambda x: (len(x), x))
    return result