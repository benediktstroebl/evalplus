
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
    # n = 0
    if n == 0:
        return []
    # n = 1
    elif n == 1:
        return []
    # n = 2
    elif n == 2:
        return [2]
    # n = 3
    elif n == 3:
        return [3]
    # n = 4
    elif n == 4:
        return [4]
    # n = 5
    elif n == 5:
        return [5]
    # ...
    else:
        prime_numbers = []
        for i in range(n+1):
            is_prime = True
            for p in range(2, i+1):
                if i % p == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(i)
        return prime_numbers