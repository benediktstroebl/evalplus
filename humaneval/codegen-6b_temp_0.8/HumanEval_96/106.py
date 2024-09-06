
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
    def count_up_to_aux(n, prime_num_list):
        if n == 1:
            return
        if n % 2 == 0:
            return count_up_to_aux(n/2, prime_num_list)
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return
        prime_num_list.append(n)
        return count_up_to_aux(n-2, prime_num_list)


    count_up_to = []
    count_up_to_aux(n, count_up_to)
    return count_up_to
