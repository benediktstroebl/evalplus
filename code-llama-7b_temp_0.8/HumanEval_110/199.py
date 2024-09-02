
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
    # 1. Mutate the lists
    lst1.append(lst2.pop())

    # 2. Check evenness
    odd = [num for num in lst1 if num % 2 == 1]

    # 3. Return "YES" if the length of the odds is less than the length of lst1
    if len(odd) < len(lst1):
        return "YES"
    return "NO"
