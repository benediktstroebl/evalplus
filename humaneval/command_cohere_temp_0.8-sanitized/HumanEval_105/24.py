def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    named_arr = []
    for num in sorted_arr:
        if 1 <= num <= 9:
            named_arr.append(NUM_TO_NAME[num])
        else:
            named_arr.append(str(num))
    return named_arr
NUM_TO_NAME = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
arr = [2, 1, 1, 4, 5, 8, 2, 3]