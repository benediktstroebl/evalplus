def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = []
    for num in sorted_arr:
        if str(num) in transf_map:
            result.append(transf_map[transf_map.index(str(num))][::-1])
    return result if result else []