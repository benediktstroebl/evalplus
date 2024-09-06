def odd_count(lst):
    r = []
    for i,n in enumerate(lst):
        # count number of odd digits
        cnt = sum(1 for c in n if c%2==1)
        # construct output string
        r.append(f"the number of odd elements {cnt}n the str{i+1}ng {i+1} of the {cnt}nput.")
    return r