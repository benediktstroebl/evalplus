def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: [x] == ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].index(x))
    return ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][::-1]*len(sorted_arr)