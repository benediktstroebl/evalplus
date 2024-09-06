
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # find the max element in the array
    max_element = max(arr)

    # create a list containing max_element and all numbers less than or equal to it
    container = [0, max_element]

    # loop through the array
    for i in range(len(arr)):
        # find the next element in the array which is not greater than or equal to the previous element
        for j in range(i, len(container)):
            # if the element is greater than the previous element
            if arr[i] > container[j]:
                # create a new list
                container = container[:j] + [arr[i]] + container[j:]
                # append the previous element to the list
                container.append(container[j-1])
                # break the for loop
                break
            # if the element is equal to the previous element
            elif arr[i] == container[j]:
                # append the previous element to the list
                container.append(container[j-1])
                # break the for loop
                break
            # if the element is less than the previous element
            elif arr[i] < container[j]:
                # append the previous element to the list
                container.append(container[j-1])

    # find the index of the largest element in the container
    for i in range(len(container)):
        if container[i] == max_element:
            return i

    # return -1 if no element is found
    return -1
