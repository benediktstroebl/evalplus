def by_length(arr):
    DIGS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    arr = sorted(arr) if arr else arr
    arr = [x for x in arr if 1 <= x <= 9]
    arr.sort(reverse=True)
    return [DIGS[i] for i in arr if i < len(DIGS)]