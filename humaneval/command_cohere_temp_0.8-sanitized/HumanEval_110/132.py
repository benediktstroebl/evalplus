def exchange(lst1, lst2):
    assert len(lst1) > 0, "Input list lst1 is empty."
    assert len(lst2) > 0, "Input list lst2 is empty."
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    count_diff_ev = sum(x % 2 == 0 for x in lst2) - even_found
    return "YES" if count_diff_ev >= 0 else "NO"