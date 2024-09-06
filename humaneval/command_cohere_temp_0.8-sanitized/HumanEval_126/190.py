def is_sorted(lst):
    return all(e <= lst[i+1] for i, e in enumerate(lst)) and len(set(lst)) == len(lst)