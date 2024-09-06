def sort_third(input_list):
    result = [input_list[i] for i in range(0, len(input_list), 3)]
    result_split = split_list(result)
    return result_split[:len(input_list)]
def split_list(lst):
    return lst[: len(lst) // 3]