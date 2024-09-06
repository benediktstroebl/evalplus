def total_match(lst1, lst2):
    char_count_1 = sum(len(x) for x in lst1)
    char_count_2 = sum(len(x) for x in lst2)
    if char_count_1 > char_count_2:
        return lst1
    elif char_count_2 > char_count_1:
        return lst2
    else:
        return lst1 if len(lst1) < len(lst2) else lst2