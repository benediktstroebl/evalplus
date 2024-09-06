def sort_third(l: list):
    l_copy = l.copy()
    return_list = []
    for i in range(len(l)):
        if i % 3 == 0:
            return_list.append(sorted(l_copy[i]))
        else:
            return_list.append(l_copy[i])
    return return_list