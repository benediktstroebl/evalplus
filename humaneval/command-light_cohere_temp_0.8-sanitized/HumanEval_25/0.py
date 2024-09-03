from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Steps:
    1. Identify the unique factorss
    prime factors
    2.
    3.
    n must be factored by a smallest prime divisor.
    until the unique primes are identified
    """

    return [d for d in range(2, int(n**0.5) + 1) if n % d == 0 for d in range(2, int(n**0.5))]