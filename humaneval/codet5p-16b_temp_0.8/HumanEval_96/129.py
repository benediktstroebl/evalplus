
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

    
    count = 1
    prime_array = []
    while count <= n:
        is_prime = True
        for i in range(2, count):
            if count % i == 0:
                is_prime = False
        if is_prime:
            prime_array.append(count)
        count += 1
    return prime_array
