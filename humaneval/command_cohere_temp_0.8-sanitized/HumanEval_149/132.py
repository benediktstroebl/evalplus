def sorted_list_sum(lst):
    lst_new = []
    for x in lst:
        if len(x) % 2 == 0:
            lst_new.append(x)
    lst_new.sort()
    for i in range(len(lst_new)):
        if i > 0 and lst_new[i] == lst_new[i - 1]:
            del lst_new[i]
            i -= 1
    return lst_new