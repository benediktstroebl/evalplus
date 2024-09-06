def is_sorted(lst):
    return all(e < lst[i+1] for i, e in enumerate(lst) if i + 1 < len(lst)) and not any(lst[i] - 1 >= lst[i+1] for i in range(len(lst)-1) if lst[i] != lst[i+1])