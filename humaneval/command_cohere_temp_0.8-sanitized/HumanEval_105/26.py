def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    named_arr = [names[int(num) - 1] for num in sorted_arr if 1 <= int(num) <= 9]
    return named_arr
names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']