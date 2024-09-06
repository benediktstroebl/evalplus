def by_length(arr):
    digits = sorted(arr, key=lambda x: 1 if x > 0 and x <= 9 else float('inf'))
    return ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][::-1]*len(digits) if digits else []