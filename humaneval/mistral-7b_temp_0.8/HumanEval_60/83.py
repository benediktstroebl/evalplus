

def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """

    # Your code here!
    # sums all integers from 1 to n.
    # n = input('Enter an integer: ')
    # sums = 0
    # for n in range(1,n):
    #     sums = sums + n
    #     print(sums)

    sums = 0
    for n in range(1,n+1):
        sums = sums + n
        print(sums)


