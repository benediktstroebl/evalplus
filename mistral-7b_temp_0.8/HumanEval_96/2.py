
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """

    #create an empty list
    list = []

    #loop through 1 to n
    for i in range(1,n+1):
        #check to see if the number is divisible by 2,3,5,7,11,13,17
        if i%2 == 0 and i%3 != 0 and i%5 != 0 and i%7 != 0 and i%11 != 0 and i%13 != 0 and i%17 != 0:
            list.append(i)
    return list

