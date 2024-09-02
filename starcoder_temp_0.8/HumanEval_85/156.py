
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_lst = []
    odd_lst = []
    result = 0
    # seperate the even and odd numbers and store them in seperate lists
    for i in range(len(lst)):
        if i % 2 == 0:
            even_lst.append(lst[i])
        else:
            odd_lst.append(lst[i])
    # if length of odd numbers is greater than or equal to even numbers, add the even numbers to result
    if len(odd_lst) >= len(even_lst):
        for i in range(len(even_lst)):
            result += even_lst[i]
    else:
        for i in range(len(odd_lst)):
            result += odd_lst[i]
    return result

