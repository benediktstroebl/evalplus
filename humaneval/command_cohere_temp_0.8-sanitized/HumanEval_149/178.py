def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        strings_with_even_length = lst[:lst_length//2]
        strings_with_odd_length = lst[lst_length//2:]
        combined_strings = strings_with_even_length + strings_with_odd_length
        combined_strings.sort()
        return combined_strings
    return lst