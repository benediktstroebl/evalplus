
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # initialize answer counter
    ans = 0
    # iterate through input array
    for num in nums:
        # split number into two parts
        split = str(num).split("-")
        # check if number is greater than 10
        if int(split[1]) > 10:
            # check if both parts are odd
            if int(split[0]) % 2 == 1 and int(split[1]) % 2 == 1:
                # increment counter
                ans += 1
    # return answer
    return ans
