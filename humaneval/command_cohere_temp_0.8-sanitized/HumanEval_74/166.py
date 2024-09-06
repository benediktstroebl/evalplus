def total_match(lst1, lst2):
    char_count_1 = sum(len(item) for item in lst1)
    char_count_2 = sum(len(item) for item in lst2)
    if char_count_1 == char_count_2:
        return lst1
    elif char_count_1 < char_count_2:
        return lst2
    else:
        return lst1