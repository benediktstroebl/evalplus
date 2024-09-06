def sort_third(input_list):
    result = []
    for i in input_list:
        if i % 3 == 0:
            result.append(sorted(input_list[i::3]))
        else:
            result.append(i)
    return result