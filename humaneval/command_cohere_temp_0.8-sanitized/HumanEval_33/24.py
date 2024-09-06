def sort_third(input_list):
    result = []
    for i in input_list:
        if i % 3 == 0:
            result.append(sorted(input_list[i]))
        else:
            result.append(input_list[i])
    return result