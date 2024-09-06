def sort_third(input_list):
    result = [x for i, x in enumerate(input_list) if i % 3 != 0]
    result.extend(sorted(input_list[i] for i in range(len(input_list)) if i % 3 == 0))
    return result