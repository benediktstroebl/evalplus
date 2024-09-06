def odd_count(lst):
    r = []
    for i,n in enumerate(lst):
        n = str(n)
        o = len([x for x in n if x % 2 != 0])
        r.append(f"the number of odd elements {o}n the str{i}ng {i} of the {i}nput.")
    return r