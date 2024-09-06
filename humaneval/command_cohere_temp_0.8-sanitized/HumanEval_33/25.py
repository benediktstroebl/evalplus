def sort_third(l: list):
    l_new = []
    for i in range(0, len(l), 3):
        try:
            temp = l[i:i+3]
            temp.sort()
            l_new.extend(temp)
        except:
            # In the case that we end the loop with a residual that is less than 3 elements, append them to l_new unsorted.
            l_new.extend(l[i:])
    return l_new