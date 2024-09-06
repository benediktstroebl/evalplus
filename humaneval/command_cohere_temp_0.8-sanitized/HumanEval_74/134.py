def total_match(lst1, lst2):
    char_count_l1 = sum(len(el) for el in lst1)
    char_count_l2 = sum(len(el) for el in lst2)
    return lst1 if char_count_l1 == char_count_l2 else lst2