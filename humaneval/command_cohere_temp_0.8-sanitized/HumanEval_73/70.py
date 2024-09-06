def smallest_change(arr):
    # initialize the transformation count
    count = 0
    # initialize the variable flag to false
    flag = False
    # traverse through the array
    for i in range(len(arr)):
        # compare the first half with the second half of the array
        if arr[i] != arr[len(arr) - 1 - i]:
            count += 1
            # check if the count is odd, if it is, the transformation is impossible
            if count % 2 == 1:
                flag = True
    # return -1 if the transformation is impossible
    if flag:
        return -1
    return count