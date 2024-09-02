
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
    # 1. let's find the middle of the list
    # 2. let's create a new list where we'll mirror the array
    # 3. we'll iterate through the mirrored array and compare the values with the first half
    # 4. if they match, we'll move to the next item
    # 5. if they don't match, we'll count them and move to the next item
    # 6. if we reach the end of the first half and we have more items to compare in the second half, we'll count them
    # 7. we'll return the minimum between the two sums
    # 8. if the array is already palindromic, we'll return 0
    arr = list(arr)
    middle = len(arr) // 2
    reverse = arr[:]
    reverse.reverse()

    def minimum(sum1, sum2):
        return sum1 if sum1 < sum2 else sum2

    # let's create a new list where we'll mirror the array
    mirror = arr[:]
    mirror.reverse()

    first_half = arr[:middle]
    second_half = mirror[middle:]

    sum1 = 0
    sum2 = 0

    for i in range(0, len(first_half)):
        if first_half[i] == second_half[i]:
            continue
        else:
            if i == middle - 1:
                for j in range(middle, len(first_half)):
                    if first_half[j] == second_half[j]:
                        continue
                    else:
                        sum1 += 1
            else:
                sum1 += 1

    return minimum(sum1, sum2)

