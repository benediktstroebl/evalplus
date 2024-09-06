
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odd_list = []
    even_list = []
    for i in nums:
        if i > 10 and (i % 2 == 1) and (i // 10 % 2 == 1):
            odd_list.append(i)
        elif i > 10 and (i % 2 == 0) and (i // 10 % 2 == 0):
            even_list.append(i)
    print(f"Number of odd elements in the array is {len(odd_list)}")
    print(f"Number of even elements in the array is {len(even_
