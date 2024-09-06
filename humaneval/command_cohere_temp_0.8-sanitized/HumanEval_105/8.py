def by_length(arr):
    digits = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    srt = sorted(arr)
    reversed_digits = [digits[int(i)] for i in srt if 1 <= int(i) <= 9 and i != '0']
    return reversed_digits if reversed_digits else []