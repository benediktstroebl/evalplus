
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Your code here
    # #To check the length of the array
    # len(arr)
    # #To access an index of an array
    # arr[0]

    # #We can also iterate over the array using range
    # #This is not a good idea as we are iterating over a list which takes O(n)
    # #This is inefficient
    # for i in range(len(arr)):
    #     print(i, arr[i])
    #     if arr[i] > arr[i + 1]:
    #         return i
    # return -1

    # Using enumerate to efficiently iterate over the array
    for index, item in enumerate(arr[:-1]):
        if item > arr[index + 1]:
            return index

    return -1
