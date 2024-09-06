
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odd = []
    new = []
    for i in nums:
        if i < 0:
            i = -i
        odd.append(i%10)
        last = i
        i = i // 10
        if i > 0:
            odd.append(i%10)
            last = i
            i = i // 10
        if last % 10 != 0:
            odd.append(last%10)
        if 10 in odd:
            odd.remove(10)
        if odd[-1] == odd[0] == odd[-1]:
            new.append(i)
            odd.clear()
    return len(new)
