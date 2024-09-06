def move_one_ball(arr):
    # if the array is empty, it is possible to sort it in non-decreasing order
    if len(arr)==0:
        return True
    # checking if the last ball (i.e. the largest number) can "swim" through the whole array
    for i in range(len(arr)-1, -1, -1):
        if arr[i] >= arr[i+1]:
            return True
    # if the largest number is smaller than the smallest number in the array, it is not possible to sort it in non-decreasing order
    return False