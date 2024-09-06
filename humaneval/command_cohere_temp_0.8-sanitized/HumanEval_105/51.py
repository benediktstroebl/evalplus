def by_length(arr):
    digits = sorted(arr, key=lambda x: 1 if x <= 1 + 9 else x // 10 if x % 10 <= 9 else x % 10)
    return ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][::-1][digits] if digits else []