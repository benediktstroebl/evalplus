def by_length(arr):
    structured = [x for x in arr if 1 <= x <= 9]
    sorted_structured = sorted(structured)
    reversed_structured = sorted_structured[::-1]
    names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [names[i] for i in reversed_structured]