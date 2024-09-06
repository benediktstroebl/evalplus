def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        # excluding odd-length strings
        filtered_list = [element for element in lst if len(element) % 2 == 0]
        # sorting them by length and alphabetically
        sorted_list = sorted(filtered_list, key=lambda x: (len(x), x))
        return sorted_list