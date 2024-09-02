
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
    # first, check if n is prime
    if n == 2:
        # if n is 2, return [2]
        return [2]
    elif n % 2 != 0:
        # if n is not prime, it can't be less than n
        return []
    else:
        # check for divisors
        divisors = [2,3,5,7]
        count = 0
        for d in divisors:
            if d <= n:
                if n % d == 0:
                    count += 1
                else:
                    break
        else:
            # if there are no divisors <= n, return an empty list
            return []
        # if there are no divisors, return an array of the first n integers that are prime numbers
        return [p for p in range(1, int(n) + 1) if not (p in divisors)]