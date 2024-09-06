def by_length(arr):
    DIGITS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    valid_digits = sorted(e for e in arr if 1 <= e <= 9)
    reversed_digits = sorted(valid_digits, reverse=True)
    return [DIGITS[i] for i in reversed_digits] if reversed_digits else []