def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        odd_len_index = [i for i, x in enumerate(lst) if len(x) % 2 == 1]
        remove_indices = [i for i in odd_len_index if i != lst_length // 2]
        removable_elements = [lst[i] for i in remove_indices]
        removable_elements.reverse()
        final_list = [x for x in lst if x not in removable_elements]
        final_list.extend(removable_elements)
        final_list.sort()
        final_list.reverse()
        return final_list