
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
    # This function uses a recursive approach to count up to n
    # The base case is when n is 0 or 1, in that case we return []
    # The recursive case is when n > 1 and n is not divisible by any of the first n-1 numbers
    # In that case, we add n to the result and call the function again with n-1
    if n <= 1:
        return []
    numbers = [2]
    while len(numbers) < n:
        numbers.append(next_prime(numbers[-1]))
    return numbers
