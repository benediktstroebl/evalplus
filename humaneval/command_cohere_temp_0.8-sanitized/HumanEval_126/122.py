def is_sorted(lst):
    return all(e < lst[i+1] for i, e in enumerate(lst) if i + 1 < len(lst)) and len(set(lst)) == len(lst)