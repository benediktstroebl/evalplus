
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    # check if array is empty
    if len(arr) == 0:
        return None
    else:
        # intialize signs array with same length as arr
        signs = [0] * len(arr)
        # intialize the sign accumulator to 1
        sign_accumulator = 1
        # intialize the product accumulator to 1
        prod_accumulator = 1
        # intialize the sum accumulator to 0
        sum_accumulator = 0

        # loop through each item in arr and update the signs array
        for i in range(len(arr)):
            # if the number in arr is 0, set the sign to 0
            if arr[i] == 0:
                signs[i] = 0
            # if the number in arr is negative, set the sign to 1
            if arr[i] < 0:
                signs[i] = 1
            # if the number in arr is positive, set the sign to -1
            if arr[i] > 0:
                signs[i] = -1

        # loop through the signs array and update the sign accumulator
        for i in range(len(signs)):
            sign_accumulator *= signs[i]

        # loop through the arr and update the product accumulator
        for i in range(len(arr)):
            prod_accumulator *= arr[i]

        # loop through the arr and update the sum accumulator
        for i in range(len(arr)):
            # if the sign of the current number is equal to the sign accumulator
            if signs[i] == sign_accumulator:
                # add the absolute value of the current number to the sum accumulator
                sum_accumulator += abs(arr[i])

        # return the product of the product and sum accumulators
        return prod_accumulator * sum_accumulator

