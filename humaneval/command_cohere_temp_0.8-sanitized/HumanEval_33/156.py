def sort_third(l: list):
    l_copy = l.copy()
    sorted_thirds = [x for x in l if x % 3 == 0 and x in sorted(l_copy)]
    return l[:len(l)//3] + sorted_thirds + l[-len(l)//3:]