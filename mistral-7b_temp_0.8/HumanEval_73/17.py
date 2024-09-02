
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # Your code here
    # use count to track amount of number in each index
    # iterate through each number and count it
    count_dict = {}
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1
    # iterate through each number and count
    # find the biggest odd number
    # subtract by 1 and add to count
    # if there are no odd numbers return 0
    # if even number is only 1 or 0 return 0
    # if there are only 2 numbers left return 1
    # if there are 3 numbers left return 2
    # if there are 4 numbers left return 3
    # if there are 5 numbers left return 4
    # if there are 6 numbers left return 5
    # if there are 7 numbers left return 6
    # if there are 8 numbers left return 7
    # if there are 9 numbers left return 8
    # if there are 10 numbers left return 9
    # if there are 11 numbers left return 
