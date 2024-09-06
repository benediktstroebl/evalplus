
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    result = []
    odd_idx = [0] * len(lst)
    for i in range(len(lst)):
        if i % 2 == 1:
            odd_idx[i] += 1
    for i in range(len(lst)):
        if odd_idx[i] >= 2:
            result.append(lst[i])
            odd_idx[i] -= 2
            for j in range(i+1, len(lst)):
                lst[j] = lst[j-1]
            break
    return result

