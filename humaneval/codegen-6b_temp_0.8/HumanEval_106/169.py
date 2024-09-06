
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)

    def sum(k):
        if k == 0:
            return 0
        else:
            return k + sum(k-1)

    def my_f(n):
        answer = []
        for i in range(0,n):
            if i%2 == 0:
                answer.append(factorial(i))
            else:
                answer.append(sum(i))
        return answer

    return my_f(n)
