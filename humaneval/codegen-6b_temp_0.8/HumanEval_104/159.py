
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
    
    # O(n) time complexity
    # O(1) space complexity
    
    power = len(str(x[0]))
    
    def split_digits(num):
        if num == 0:
            return []
        
        digits = []
        while num > 0:
            digit = (num % 10)
            digits.append(digit)
            num = (num - digit) // 10
            
        return digits
            
    for num in x:
        digit_list = split_digits(num)
        if sum(digit_list) % 2 != 0:
            answer = digit_list
            break
            
    return answer
