def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x < 1 or x > 9 else x)
    reverse_arr = sorted(sorted_arr, reverse=True)
    result = [name for num, name in enumerate(
        ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'], 1)
        if reverse_arr[num] == num]
    return result if result else []