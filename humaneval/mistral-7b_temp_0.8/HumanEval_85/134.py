
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """


    a=lst[:]
    sum=0
    for i in range(len(a)):
        if a[i]%2==0 and i%2!=0:
            sum=sum+a[i]
    return sum

    # Return an integer
    # Get the sum of the even elements that are at odd indices..
    # You can assume that the length of the list is positive.
    # Examples:
    #     add([4, 2, 6, 7]) ==> 2
    #     add([4, 2, 10, 7]) ==> 4
    #     add([4, 2, 10, 7, 5, 20]) ==> 20







    # print(a)
    # for i in range(len(a)):
    #     print(a[i])
    #     if a[i]%2==0 and i%2!=0:
    #         print(a[i])
    #         # sum=sum+a[i]
    #         # print(sum
