
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    lst1_even = all([num % 2 == 0 for num in lst1])
    if lst1_even:
        return "YES"
    lst2_odd = all([num % 2 == 1 for num in lst2])
    if lst2_odd:
        return "NO"
    odd_idx = next(
        idx for idx, num in enumerate(lst1) if num % 2 == 1)
    even_idx = next(
        idx for idx, num in enumerate(lst2) if num % 2 == 0)
    lst1[odd_idx], lst2[even_idx] = lst2[even_idx], lst1[odd_idx]
    return "YES" if all([num % 2 == 0 for num in lst1]) else "NO"

