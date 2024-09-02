
def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """

    # Please write your code here
    if n == 0:
        return []
    elif n == 1:
        return [3]
    else:
        list1 = []
        if n % 2 == 0:
            list1.append(3)
            for i in range(1, n):
                if i % 2 == 0:
                    list1.append(1 + (i / 2))
        else:
            list1.append(3)
            for i in range(1, n):
                if i % 2 != 0:
                    list1.append(list1[-1] + list1[-2] + list1[-3])
    return list1

