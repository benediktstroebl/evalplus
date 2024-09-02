
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    # your code here
    #initialze a variable to hold the count
    count = 0
    #iterate over the array
    for num in arr:
        #initialze a variable to hold the total sum
        total = 0
        #use while loop to iterate over the digits of a number
        while num > 0:
            #add the last digit to the total sum
            total += num % 10
            #update the number by dividing it by 10
            num = num // 10
        #if the total sum is greater than 0, add 1 to the count variable
        if total > 0:
            count += 1
    return count
