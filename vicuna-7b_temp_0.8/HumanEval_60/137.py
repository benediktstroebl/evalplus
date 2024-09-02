

def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    # check if n is 0
    if n == 0:
        return 0
    
    # check if n is 1
    if n == 1:
        return 1
    
    # iterate over numbers from 1 to n
    for i in range(1, n+1):
        # add i to the result
        result = i
        # loop over the numbers from 1 to n-1
        for j in range(2, n):
            # subtract i from the result if it is greater or equal to j
            if result >= j:
                result -= i
            else:
                # subtract the result from j
                result = j - result
        
        # update the result with the current value
        result += i
        
        # print the result
        print(result)
        
        
