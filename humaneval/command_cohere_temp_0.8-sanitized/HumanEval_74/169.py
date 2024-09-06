def total_match(lst1, lst2):
    char_count_list1 = sum(len(x) for x in lst1)
    char_count_list2 = sum(len(x) for x in lst2)
    if char_count_list1 == char_count_list2:
        return lst1 if lst1 == lst2 else lst2 
    return lst1 if char_count_list1 < char_count_list2 else lst2