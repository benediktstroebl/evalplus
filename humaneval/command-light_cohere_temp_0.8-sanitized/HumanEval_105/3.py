def by_length(arr):
    if not arr:  # if the array is empty
        return []

    # sort array elements from 1 to 9
    arr.sort()

    arr = [i for i in arr if i >= 1 and i <=9]
    # reverse the array
    arr.reverse()
    array_str= str(arr)
    # replace each digit with its corresponding name
    arr = [int("One")] + arr

    return arr