def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [ele for ele in sorted_arr if 1 <= ele <= 9]
    reversed_digits = filtered_digits[::-1]
    names = []
    for ele in reversed_digits:
        names.append(ele_to_name(ele))
    return names if names else []
def ele_to_name(ele):
    """Constants for digit names"""
    DIGITS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return DIGITS[ele - 1] if 0 <= ele - 1 < len(DIGITS) else ''