def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x <= 9 else x)
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    named_arr = [
        "One" if x == 1 else
        "Two" if x == 2 else
        "Three" if x == 3 else
        "Four" if x == 4 else
        "Five" if x == 5 else
        "Six" if x == 6 else
        "Seven" if x == 7 else
        "Eight" if x == 8 else
        "Nine" if x == 9 else
        str(x)
        for x in reversed_sorted_arr
    ]
    return named_arr