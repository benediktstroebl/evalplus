
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
    list1 = [1, 1, 1]
    list2 = [0, 1, 1]
    list3 = [1, 1, 0]
    list4 = [1, 0, 1]
    list5 = [1, 0, 0]
    list6 = [1, 0, 0, 1]
    list7 = [1, 0, 0, 0]
    list8 = [1, 0, 0, 0, 1]
    list9 = [1, 0, 0, 0, 0]
    list10 = [1, 0, 0, 0, 0, 1]
    list11 = [1, 0, 0, 0, 0, 0]
    list12 = [1, 0, 0, 0, 0, 0, 1]
    list13 = [1, 0, 0, 0, 0, 0, 0]
    list14 = [1, 0, 0, 0, 0, 0, 0, 1]
    list15 = [1, 0, 0, 0, 0, 0, 0, 0]
    for i in range(n + 1):
        list1[i] = (list1[i - 1] + list2[i - 1] + list3[i - 1]) % 10
        list2[i] = (list1[i] + list2[i - 1] + list4[i - 1]) % 10
        list3[i] = (list1[i] + list2[i] + list5[i - 1]) % 10
        list4[i] = (list1[i] + list2[i] + list6[i - 1]) % 10
        list5[i] = (list1[i] + list2[i] + list7[i - 1]) % 10
        list6[i] = (list1[i] + list2[i] +
