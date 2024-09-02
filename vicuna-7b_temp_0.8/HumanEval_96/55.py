
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
    prime_numbers = [2,3,5,7,11,13,17,19]
    n = n//1
    i = 0
    while i < n:
        if n % i:
            i += 1
        else:
            n = n//i
            yield prime_numbers[i-1]
            i += 1
\end{code}

I'm trying to use this function as a test function in my code, but the test is failing.