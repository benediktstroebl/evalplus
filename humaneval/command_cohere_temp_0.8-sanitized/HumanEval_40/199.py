def triples_sum_to_zero(lst):
    # Sort the list in order to make the candidates for the triple be next to each other.
    lst.sort()
    for a in lst:
        for b in lst:
            if a != b and b - a == 0:
                temp = lst[len(lst) - 1]
                if temp == a - b or temp == b - a:
                    return True
                break
        if b == 0:
            break
    return False