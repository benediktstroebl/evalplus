def by_length(arr):
    numbered = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    filtered = [x for x in arr if 1 <= x <= 9]
    sorted_filtered = sorted(filtered)
    reversed_sorted = sorted_filtered[::-1]
    result = [numbered[digit - 1] for digit in reversed_sorted if digit <= 9]
    return result if result else []