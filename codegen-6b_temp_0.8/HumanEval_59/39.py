

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    n_list = n.to_list("F")
    for i in range(len(n_list)):
        if n_list[i] != '0':
            test = 2
            while(i + 1 < len(n_list) and test <= n_list[i]):
                if n_list[i + 1] % test == 0:
                    break
                test += 1
            if test > n_list[i]:
                n_list[i] = test
    return int("".join(n_list))