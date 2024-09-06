def by_length(arr):
    digits = sorted(arr, key=lambda x: 1 if x > 0 and x <= 9 else float('inf'))
    return [name for digit in reversed(digits) for name in {'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'} if digit == name[0]] if digits else []