
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    result = [1]
    while len(result) < n:
        # find the number of even indices
        idx = 0
        while idx < n and result[idx] % 2 == 0:
            idx += 1
        if idx == n:
            # append the factorial of each even index
            for i in range(1, idx + 1):
                result.append(i)
        else:
            # append the sum of numbers from 1 to each index
            for i in range(1, idx + 1):
                result.append(i + (n - idx))
    return result
