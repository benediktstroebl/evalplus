def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [ele for ele in sorted_arr if 1 <= ele <= 9]
    reversed_digits = filtered_digits[::-1]
    names = []
    for ele in reversed_digits:
        names.append(ele_to_name(ele))
    return names if names else []
def ele_to_name(ele):
    dict_map = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    return dict_map[ele] if ele in dict_map else ""
arr = [2, 1, 1, 4, 5, 8, 2, 3]