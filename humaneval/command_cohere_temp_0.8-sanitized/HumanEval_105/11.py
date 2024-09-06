def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x <= 9 else x)
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    result = [name for num in reversed_sorted_arr for name in num_to_name[num]]
    return result
num_to_name = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}