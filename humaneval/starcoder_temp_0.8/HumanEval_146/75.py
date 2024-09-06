
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    return len([num for num in nums if num > 10 and num % 10 in (1, 3, 5, 7, 9) and num % 100 in (11, 13, 17, 19, 31, 33, 37, 39, 71, 73, 77, 79) and num % 1000 in (111, 113, 117, 119, 131, 137, 139, 171, 173, 177, 179, 191, 193, 197, 199, 311, 313, 317, 319, 331, 337, 339, 371, 373, 377, 379, 391, 393, 397, 399, 711, 713, 717, 731, 737, 739, 771, 773, 777, 791, 797, 799, 911, 919, 931, 937, 971, 977, 991, 993, 997])])
