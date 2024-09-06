def sort_third(input_list):
    result = []
    for i in input_list:
        if i % 3 == 0:
            result.append(sorted([x for x in input_list if x % 3 == i % 3 and x != i][0]))
        else:
            result.append(i)
    return result