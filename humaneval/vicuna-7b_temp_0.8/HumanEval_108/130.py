
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
    def _sum(x):
        return sum(map(int, x))
    
    def count_nums_helper(arr, sum_so_far):
        if not arr:
            return sum_so_far
        else:
            curr_sum = _sum(arr)
            for i in range(1, len(arr)):
                arr_len = len(arr)
                curr_num = arr[i]
                next_num = arr[i+1]
                curr_sum += int(curr_num)
                curr_sum += int(next_num)
                if (curr_num > 0 and curr_num < 10) or (curr_num > 10 and next_num > 0):
                    sum_so_far += 1
            return sum_so_far
    
    return count_nums_helper(arr, 0)
