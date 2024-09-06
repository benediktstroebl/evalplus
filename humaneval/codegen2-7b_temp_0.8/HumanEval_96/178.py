
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
    if n == 0:
        return []
    if n < 2:
        return []
    prime_list = []
    prime_nums = []
    for i in range(1, n+1):
        if i == 1:
            prime_list.append(i)
        else:
            if i % 2 == 0:
                prime_list.append(i)
            else:
                for num in prime_list:
                    if i % num == 0:
                        break
                else:
                    prime_list.append(i)
    prime_list = [2] + prime_list
    return prime_list
