
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
    # YOUR CODE HERE
    if not lst1 or not lst2:
        return None
    lst1_even = []
    lst2_even = []
    for num in lst1:
        if num % 2 == 0:
            lst1_even.append(num)
    for num in lst2:
        if num % 2 == 0:
            lst2_even.append(num)
    lst1_diff = abs(len(lst1_even) - len(lst2_even))
    if lst1_diff > 1:
        return False
    elif lst1_diff == 1:
        if lst1_even[0] > lst2_even[0]:
            return False
        else:
            return True
    else:
        return True

