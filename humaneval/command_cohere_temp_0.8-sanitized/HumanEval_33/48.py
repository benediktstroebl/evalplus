def sort_third(l: list):
    l_copy = l.copy()
    sorted_thirds = [y for x, y in enumerate(l) if x % 3 == 0 and l[x] != l[x-1] and l[x] != l[x+1] and x != 0]
    sorted_thirds.sort()
    for i in range(len(l)):
        if i % 3 == 0 and l[i] != sorted_thirds[0] and l[i] != l[i-1] and l[i] != l[i+1]:
            l[i] = sorted_thirds[0]
    return l