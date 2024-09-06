
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    
    def even_digit(num):
        if num == 0:
            return True
        else:
            while num > 0:
                if num % 2 == 0:
                    return True
                else:
                    num = num // 10
            return False

    def string_to_digit(num):
        n = 0
        for digit in num:
            n = n * 10 + int(digit)
        return n

    def digit_to_string(num):
        return str(num)

    def is_sorted(num):
        for i in range(len(num) - 1):
            if int(num[i]) > int(num[i + 1]):
                return False
        return True

    ans = []
    for num in x:
        if len(str(num)) > 1 and even_digit(num):
            continue
        else:
            num = string_to_digit(str(num))
            if not num in ans:
                ans.append(num)
                continue
    if is_sorted(ans):
        return sorted(ans)
