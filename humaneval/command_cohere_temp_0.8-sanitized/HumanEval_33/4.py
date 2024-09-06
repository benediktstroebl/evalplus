def sort_third(l: list):
    l_new = []
    for i in range(0, len(l), 3):
        try:
            temp = l[i:i+3]
            temp.sort()
            l_new.extend(temp)
        except:
            # In the case where we would divide beyond the list length, append the remaining element and move on
            l_new.append(l[i])
    return l_new