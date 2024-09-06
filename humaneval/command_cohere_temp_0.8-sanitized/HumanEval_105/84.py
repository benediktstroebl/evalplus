def by_length(arr):
    # sort and reverse the array
    sorted_arr = sorted(arr)
    reversed_arr = sorted_arr[::-1]
    # convert sorted and reversed digits into names
    result = ['None'] * len(reversed_arr)
    for i, num in enumerate(reversed_arr):
        if 1 <= num <= 9: 
            result[i] = NUM_TO_NAME[num]
    return result
NUM_TO_NAME = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9}