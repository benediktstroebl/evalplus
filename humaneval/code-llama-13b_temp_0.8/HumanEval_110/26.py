
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

    lst1_evens = [i for i in lst1 if i % 2 == 0]
    lst2_odds = [i for i in lst2 if i % 2 == 1]
    lst2_odds_set = set(lst2_odds)
    lst1_evens_set = set(lst1_evens)

    for odd in lst2_odds:
        for even in lst1_evens:
            if odd == even:
                continue
            if odd + even == 0:
                return "NO"
            if (odd + even) % 2 == 0 and odd + even in lst2_odds_set:
                lst2_odds_set.remove(odd + even)
                lst1_evens_set.add(odd)
            if len(lst2_odds_set) == 0 and len(lst1_evens_set) == len(lst1_evens):
                return "YES"
    return "NO"
