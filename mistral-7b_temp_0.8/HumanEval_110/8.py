
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
    print('Enter the first list')
    lst1 = [int(n) for n in input().split()]
    print('Enter the second list')
    lst2 = [int(n) for n in input().split()]

    # Write your code here
    if len(lst1) != len(lst2):
        print('NO')
    elif all([i % 2 == 0 for i in lst1]) or all([i % 2 == 0 for i in lst2]):
        print('YES')
    else:
        print('NO')


