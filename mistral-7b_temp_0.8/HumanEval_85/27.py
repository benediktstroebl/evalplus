
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # your code here
    count = 0
    even_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
            count += 1
        if count == 2:
            break

    # print(even_list)
    return sum(even_list)

