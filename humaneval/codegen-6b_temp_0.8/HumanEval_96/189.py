
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
    # the last element of the array is the number n
    output = []
    prime = 2
    while len(output) < n:
        output.append(prime)
        prime += 1
        for potential_factor in range(prime, n+1):
            if potential_factor % prime == 0 and potential_factor != prime:
                break
        else:
            prime += 1
    return output
