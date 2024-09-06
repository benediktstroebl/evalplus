def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = []
    for num in sorted_arr:
        if 1 <= num <= 9:
            result.append(transf_map[num - 1])
        else:
            result.append(str(num))
    return result if result else []