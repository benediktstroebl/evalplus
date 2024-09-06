
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return []
    else:
        for i in range(len(lst)):
            if i % 2 == 1:
                if lst[i] > lst[i+1]:
                    j = i
                else:
                    j = i + 1
                lst[j],lst[i] = lst[i],lst[j]
                break
        return lst[1:] + lst[:i]