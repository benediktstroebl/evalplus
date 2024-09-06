
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    
    # Time: O(n)
    # Space: O(n)
    
    # one liner
    # return [
    #     1 if n % 2 == 0 else n + sum(range(1, n//2 + 1))
    # ]
    
    # [1] more general
    # [1, 2, 6, 24, 15]
    
    # [1, 1, 1, 1, 1]
    result = [1] * n
    
    for i in range(1, n, 2):
        result[i] = result[i - 1] * i
    
    return result


assert f(5) == [1, 2, 6, 24, 15]
assert f(3) == [1, 4, 15]
assert f(1) == [1]
assert f(1) == [1]
assert f(2) == [1]
assert f(2) == [1]
assert f(1) == [1]
assert f(2) == [1]
assert f(2) == [1]
assert f(4) == [1, 2, 6, 24]
assert f(5) == [1, 2, 6, 24, 15]
assert f(6) == [1, 2, 6, 24, 15, 85]
assert f(8) == [1, 2, 6, 24, 15, 85, 680, 632, 656]
assert f(10) == [1, 2, 6, 24, 15, 85, 680, 632, 656, 46617, 644102, 654320]
