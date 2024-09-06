def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    res = [transf_map[int(num) - 1] for num in sorted_arr if 1 <= int(num) <= 9]
    return res if res else []