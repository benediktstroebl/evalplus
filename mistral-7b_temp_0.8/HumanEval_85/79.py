
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Your code here
    for i,j in enumerate(lst):
        if(i%2==1):
            if j%2==0:
                print(j)
    return
