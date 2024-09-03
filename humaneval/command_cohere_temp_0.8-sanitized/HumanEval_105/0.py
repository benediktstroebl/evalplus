def by_length(arr):
    sorted_arr = sorted(arr, key = lambda x: 1 if x <= 9 else x)
    reversed_sorted_arr = sorted(sorted_arr, reverse = True)
    result = []
    for num in reversed_sorted_arr:
        if 1 <= num <= 9:
            result.append(NUM_TO_NAME[num])
    return result if result else []
NUM_TO_NAME = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9}