
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # SpecialFilter(nums)
    # if the number is greater than 10
    # and first and last number of the number are odd
    # return the number of element
    # else return 0

    # nums = [15, -73, 14, -15]
    # nums = [33, -2, -3, 45, 21, 109]

    # nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109]
    # # function(nums)
    # # for i in nums:
    # #     if i > 10:
    # #         print(i)
    # #         if i % 10 == 1 or i % 10 == 9:
    # #             print(i)
    #
