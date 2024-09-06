def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        odd_length_words = [word for word in lst if len(word) % 2 == 1]
        return sorted(set(lst) - set(odd_length_words))