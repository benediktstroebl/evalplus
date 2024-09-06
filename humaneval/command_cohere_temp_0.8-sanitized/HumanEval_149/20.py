def sorted_list_sum(lst):
    lst_new = []
    for string in lst:
        if len(string) % 2 == 0:
            lst_new.append(string)
    # Sorting the list in ascending order
    lst_new.sort()
    # Sorting the list in alphabetical order
    lst_new.sort(key=str.lower)
    return lst_new