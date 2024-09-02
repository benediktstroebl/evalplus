
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    for i in range(n-1,-1,-1):
        even = 0
        for j in range(i+1,n):
            if(lst[j]%2 == 0):
                even += lst[j]
        lst[i:even] = [lst[i]]
        lst = [lst[i+1] for i in range(len(lst)-1)]

lst = [6, 3, 4, 1, 7, 9]
