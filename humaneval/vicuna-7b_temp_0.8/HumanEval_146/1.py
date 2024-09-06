
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # Use a counter to count the number of elments that match the condition
    nums_filtered = []
    for num in nums:
        filtered = True
        for i in range(len(num)-1, -1, -1):
            if num[i] == num[i+1]:
                if (num[i] % 2 != 0 and num[i+1] % 2 != 0):
                    filtered = False
                break
        if filtered:
            nums_filtered.append(num)
    return len(nums_filtered)
