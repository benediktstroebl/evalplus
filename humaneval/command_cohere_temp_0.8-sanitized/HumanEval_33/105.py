def sort_third(input_list):
    result = [input_list[i] for i in range(0, len(input_list), 3)]
    result_split = split_into_thirds(result)
    return result_split[:len(input_list)]
def split_into_thirds(lst):
    return [lst[i:i+3] for i in range(0, len(lst), 3)]