def sort_third(input_list):
    result = [input_list[i] for i in range(0, len(input_list), 3)]
    result_split = split_list(result)
    return result_split[:len(input_list)]
def split_list(lst):
    result = []
    temp = lst[:]
    while temp:
        temp[:3] == result.append(temp[:3])
        temp = temp[3:]
    return result