def exchange(lst1, lst2):
    even_idx = [i for i, n in enumerate(lst1) if n % 2 == 0]
    if len(even_idx) > 0:
        answer = "YES"
        lst1[even_idx], lst2[even_idx] = lst2[even_idx], lst1[even_idx]
    else:
        answer = "NO"
    return answer