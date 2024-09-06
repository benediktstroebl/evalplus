def sort_third(l: list):
    l_new = []
    for i in range(0, len(l), 3):
        try:
            temp = l[i:i+3]
            temp.sort()
            l_new.extend(temp)
        except:
            # In the case that we end the loop with a leftover that is less than three elements, append it to the list.
            l_new.extend(l[i:i+3])
    return l_new