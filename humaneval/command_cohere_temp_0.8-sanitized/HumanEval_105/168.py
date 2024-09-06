def by_length(arr):
    sorted_arr = sorted(arr)
    stripped_arr = [str(n) for n in sorted_arr if 1 <= n <= 9]
    stripped_arr.reverse()
    result = [name for num in stripped_arr for name in num_to_name[num]]
    return result
num_to_name = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}