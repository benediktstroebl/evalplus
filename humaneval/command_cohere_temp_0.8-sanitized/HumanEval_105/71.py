def by_length(arr):
    sorted_arr = sorted(arr)
    sorted_arr = sorted_arr[::-1]
    transf = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = [transf[int(num) - 1] for num in sorted_arr if int(num) >= 1 and int(num) <= 9]
    return result if result else []