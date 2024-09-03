def max_element(lst):
    if not_unique(lst) == False:
        raise ValueError("Input list must contain unique elements")
    return max(lst)