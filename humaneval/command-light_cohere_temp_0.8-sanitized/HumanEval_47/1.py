def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n-1)//2][0] + lst[n//2][0]) / 2
    else:
        return lst[(n-1)//2][0]