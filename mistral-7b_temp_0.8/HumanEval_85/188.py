
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # add your code here
    if len(lst) == 0:
        return 0
    else:
        odd_indx = 0
        even_val = 0
        for i in range(len(lst)):
            if i % 2 != 0:
                if lst[i] % 2 == 0:
                    even_val += lst[i]
                    odd_indx += 1
                    if odd_indx % 2 != 0:
                        return even_val
        return 0
