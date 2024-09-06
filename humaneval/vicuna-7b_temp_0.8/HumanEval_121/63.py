
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Using sieve of Eratosthenes, find all prime numbers in the range
    primes = [True] * (int(math.sqrt(len(lst))) + 1)
    for i in range(2, len(lst)):
        if lst[i] % primes[i] == 0:
            primes[i] = False
    odd_pos = [i for i in range(len(lst)) if lst[i] % 2 == 1 and lst[i] not in primes]
    return sum(odd_pos)
