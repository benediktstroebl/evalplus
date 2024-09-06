
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

    if n == 0:
        return []

    else:
        if n == 1:
            return [3]

        elif n == 2:
            return [3, 1]

        else:
            first = [3, 1]
            second = [3, 1, 2]
            third = [3, 1, 2, 8]
            num = len(third)
            temp = []

            if n % 2 == 0:
                n = n + 1
                temp.append(3)
                for i in range(0, n):
                    temp.append(temp[-2] + temp[-1])

            else:
                n = n - 2
                for i in range(2, n + 3):
                    temp.append(first[i] + second[i - 1] + third[i - 2])

            return temp
