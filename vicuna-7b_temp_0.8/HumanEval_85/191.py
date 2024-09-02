
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    odd_indices = [i for i in range(len(lst)) if (lst[i] % 2) != 0]
    even_lst = []
    for i in odd_indices:
        even_lst.append(lst[i])
    return sum(even_lst)

lst = [1, 2, 3, 4, 5, 6]
print(add(lst))