
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return []
    else:
        odd_indices = [0]
        even_lst = []
        for num in lst:
            if num % 2 == 0:
                even_lst.append(num)
            else:
                odd_indices.append(len(even_lst))
        return odd_indices[::-1] + even_lst

print(add([4, 2, 6, 7]))
