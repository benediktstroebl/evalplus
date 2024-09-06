def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: x if 1 <= x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    named_reversed_arr = [
        'One', 'Two', 'Three', 'Four',
        'Five', 'Six', 'Seven', 'Eight', 'Nine'
       ][::-1].__getitem__
    
    return named_reversed_arr(reversed_sorted_arr) if reversed_sorted_arr else []