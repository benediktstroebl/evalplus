
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # [15, -73, 14, -15]
    # [33, -2, -3, 45, 21, 109]

    # 1) create an array of numbers that are greater than 10 and both first and last digits of a number are odd.
    # 2) return the length of that array

    # 1) create an array of numbers that are greater than 10 and both first and last digits of a number are odd.
    # specialArray = []
    # for num in nums:
    #     if num > 10:
    #         # check if first and last digits are odd
    #         if num % 10 != 0:
    #             # compare the digits at first and last indices of the number
    #             if num // 10 % 10 != 0:
    #                 specialArray.append(num)

    # return len(specialArray)

    # 2) return the length of that array
    # return len(specialArray)

    # filteredArray = []
    # for num in nums:
    #     if num > 10:
    #         # check if first and last digits are odd
    #         if num % 10 != 0:
    #             # compare the digits at first and last indices of the number
    #             if num // 10 % 10 != 0:
    #                 filteredArray.append(num)

    # return len(filteredArray)

    # create an array of numbers that are greater than 10 and both first and last digits of a number are odd.
    # and return the length of that array
    return len([num for num in nums if num > 10 and num % 10 != 0 and num // 10 % 10 != 0])
