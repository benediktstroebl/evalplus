
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # YOUR CODE HERE
    lst2=[]
    if lst:
        for i in range(1,len(lst),2):
            if lst[i]%2==0:
                lst2.append(lst[i])
        if lst2:
            print(lst2)
        else:
            print(0)

