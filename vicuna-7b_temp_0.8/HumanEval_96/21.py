
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
    # Check if n is 0 or prime and less than 2
    if n == 0 or n % 2 == 0:
        return []
    # For n-1
    for i in range(2, n + 1):
        if n % i == 0:
            return []
        if (n % i) == 1:
            prime_list = []
            for j in range(i + 1, n + 1):
                if (n % j) == 1:
                    prime_list.append(j)
                    break
            return prime_list
    return []