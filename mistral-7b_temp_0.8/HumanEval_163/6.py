
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # your code here
    # list1=[]
    # if a<b:
    #     for i in range(a,b+1):
    #         if i%2==0:
    #             list1.append(i)
    # return list1
    # else:
    #     for i in range(b,a-1,-1):
    #         if i%2==0:
    #             list1.append(i)
    #     return list1
    # print(list1)
    a1=a
    b1=b
    if a>b:
        a1=b1
        b1=a1
    list1=[]
    for i in range(a1,b1+1):
        if i%2==0:
            list1.append(i)
    return list1

