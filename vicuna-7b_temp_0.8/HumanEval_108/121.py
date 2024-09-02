
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
    def count_sign_digits(num):
        sign = num // 2
        if num % 2 != 0:
            num += 1
        return sign, num
    
    def count_nums_helper(arr, sum_so_far):
        if not arr:
            return sum_so_far
        
        for i in range(len(arr)):
            sum_so_far += arr[i]
            if sum_so_far >= 10:
                count_nums_helper(arr, sum_so_far % 10)
            elif sum_so_far % 2 == 0:
                count_nums_helper(arr, sum_so_far)
            
        return sum_so_far
    
    return count_nums_helper(arr, 0)
