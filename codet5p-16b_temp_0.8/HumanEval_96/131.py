
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

    assert type(n) is int and n >= 0
    arr = [2,3]
    for num in range(5, n+1):
        flag = True
        for i in arr:
            if num % i == 0:
                flag = False
                break
        if flag:
            arr.append(num)
    return arr
