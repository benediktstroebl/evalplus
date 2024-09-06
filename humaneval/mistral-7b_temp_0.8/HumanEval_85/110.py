
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    def add(lst):
        if len(lst)==0:
            return 0
        if lst[0]%2==0 and lst[0]%2!=0:
            return add(lst[1:])+lst[0]
        return add(lst[1:])


    # Your code here


    return add(lst)
