def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
        5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
        9: 'Nine'
    }
    result = [transf_map[int(i)] for i in sorted_arr if i in transf_map]
    return result if result else []