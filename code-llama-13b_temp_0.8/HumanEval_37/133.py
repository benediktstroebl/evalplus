

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    n = len(l)
    l_prime = [0]*n
    for i in range(n):
        if i%2==0:
            l_prime[i] = l[i]
        else:
            j = 0
            while l[i] > l[j]:
                j += 2
            if j >= i:
                l_prime[i] = l[i]
            else:
                l_prime[i] = l[j]
                l_prime[j] = l[i]
    return l_prime
