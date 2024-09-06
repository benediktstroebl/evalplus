
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    even_lst = [lst[i] for i in range(n // 2)]
    odd_lst = [lst[i] for i in range(n // 2, n)]
    result = []
    for i in range(n):
        if i % 2 == 1:
            result.append(even_lst[i])
    return result

print(add([2, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15]))
