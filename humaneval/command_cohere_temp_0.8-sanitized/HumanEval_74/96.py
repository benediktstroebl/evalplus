def total_match(lst1, lst2):
    char_count_lst1 = sum(len(el) for el in lst1)
    char_count_lst2 = sum(len(el) for el in lst2)
    if char_count_lst1 == char_count_lst2:
        return lst1
    elif char_count_lst1 < char_count_lst2:
        return lst1
    elif char_count_lst1 > char_count_lst2:
        return lst2
    else:
        return []