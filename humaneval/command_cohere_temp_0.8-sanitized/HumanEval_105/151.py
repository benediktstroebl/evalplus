def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = [transf_map[int(num) - 1] for num in sorted_arr if num >= 1 and num <= 9]
    return result if result else []