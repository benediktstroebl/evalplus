def sort_third(input_list):
    result = [input_list[i] for i in range(0, len(input_list), 3)]
    result_split = iter(result)
    return [next(result_split), next(result_split), next(result_split)]