def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        strings_with_even_length = []
        for string in lst:
            if len(string) % 2 == 0:
                strings_with_even_length.append(string)
        return strings_with_even_length