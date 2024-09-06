def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    numbered_arr = [str(item) for item in sorted_arr if 1 <= item <= 9]
    return ['Zero' if not numbered_arr else ''.join(numoded_arr)]