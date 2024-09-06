
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
    if n == 1:
        return []
    count = 0
    list = []
    for i in range(2,n):
        if i == 2:
            list.append(2)
            count+=1
        if i%2 != 0:
            for j in range(3,n,2):
                if j == 3:
                    list.append(3)
                    count+=1
                if j%3 == 0:
                    break
                if j%2 == 0:
                    continue
        for j in range(5,n,2):
            if j%5 == 0:
                break
            if j%3 == 0:
                continue
            if j%2 == 0:
                continue
            if j%7 == 0:
                break
            if j%5 == 0:
                continue
            if j%2 == 0:
                continue
            if j%11 == 0:
                break
            if j%5 == 0:
               
