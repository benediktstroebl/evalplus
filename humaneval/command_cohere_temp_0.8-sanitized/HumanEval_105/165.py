def by_length(arr):
    validated_arr = [x for x in arr if 1 <= x <= 9]
    sorted_arr = sorted(validated_arr)
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    names = []
    for num in reversed_sorted_arr:
        names.append({"One": "One", "Two": "Two", "Three": "Three", "Four": "Four", "Five": "Five", "Six": "Six", "Seven": "Seven", "Eight": "Eight", "Nine": "Nine"}[str(num)])
    return names