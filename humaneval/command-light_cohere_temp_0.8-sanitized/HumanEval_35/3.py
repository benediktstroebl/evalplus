def max_element(lst):
    if not_elements(lst):  # Checks for empty list
        return None
    
    max_ = max(lst)
    min_ = min(lst)
    if max >= min:
        return max
    else:
        return min