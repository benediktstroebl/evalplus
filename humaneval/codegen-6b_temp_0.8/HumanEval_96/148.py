
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
    if n < 0:
        return []
    if n == 0:
        return []
    elif n == 1:
        return [2]
    elif n == 2:
        return [2, 3]
    else:
        return_list = [2]
        k = 3
        while k <= n:
            i = 2
            temp = k
            while i <= temp:
                if temp % i == 0:
                    break
                i += 1
            if i == temp:
                return_list.append(temp)
            k += 1
        return return_list

