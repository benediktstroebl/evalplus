
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    def sum_digits(n):
        """
        Compute the sum of the digits of a number.
        """
        sum = 0
        while n > 0:
            sum = sum * 10 + n % 10
            n = div(n, 10)
        return sum

    def count(n):
        """
        Compute the number of negative numbers with the given absolute value.
        """
        return sum([-count(abs(d)) for d in str(n)])

    def count_total(n):
        """
        Compute the number of negative and positive numbers with the given absolute value.
        """
        return sum([count(abs(d)) for d in str(n)])

    def count_nums_helper(arr, i, n):
        """
        Recursive function that counts the number of negative numbers <= n
        in the subarray.
        """
        if i == len(arr) - 1 and arr[i] < n:
            return 0
        elif arr[i] >= n:
            return count(arr[i])
        else:
            count_nums_helper(arr, i+1, n-arr[i])
            return count_nums_helper(arr, i+1, n)

    count_nums_total = count_nums_helper

    return count_nums_total(arr, 0)
