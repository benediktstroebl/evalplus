def sort_third(input_list):
    result = [x for i, x in enumerate(input_list) if i % 3 != 0]
    result.extend(sorted(input_list[i] for i in range(0, len(input_list), 3) if i % 3 == 0))
    return result