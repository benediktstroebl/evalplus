def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        temp = lst.copy()
        temp.sort()
        result = []
        for i in range(lst_length // 2):
            result.append(temp[i])
        for i in range(lst_length // 2, lst_length):
            if temp[i] != temp[i - lst_length // 2]:
                result.append(temp[i])
        return result
    else:
        temp = lst.copy()
        temp.sort()
        result = []
        for i in range(lst_length // 2 + 1):
            result.append(temp[i])
        return result