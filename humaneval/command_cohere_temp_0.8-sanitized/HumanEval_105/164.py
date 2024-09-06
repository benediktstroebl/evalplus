def by_length(arr):
    sorted_arr = sorted(arr)
    stripped_arr = [str(ele) for ele in sorted_arr if 1 <= ele <= 9]
    stripped_arr.reverse()
    digit_names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [name for name, num in zip(digit_names, stripped_arr) if num != '' ]