
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # solution 1 - iterate from the back of the list
    # arr = [1, 2, 4, 3, 5]
    # idx = len(arr) - 2
    # while idx >= 0:
    #     if arr[idx] > arr[idx+1]:
    #         break
    #     idx -= 1
    # if idx == -1:
    #     return -1
    # return idx

    # solution 2 - iterate from the front of the list
    # arr = [1, 2, 4, 3, 5]
    # idx = 0
    # while idx + 1 < len(arr):
    #     if arr[idx] > arr[idx + 1]:
    #         break
    #     idx += 1
    # if idx == len(arr) - 1:
    #     return -1
    # return idx

    # solution 3 - use a dictionary
    # arr = [1, 2, 4, 3, 5]
    # d = {}
    # for idx, num in enumerate(arr):
    #     d[num] = idx
    # sorted_nums = sorted(arr)
    # for idx, num in enumerate(sorted_nums[:-1]):
    #     if num > sorted_nums[idx + 1]:
    #         return d[num]
    # return -1

    # solution 4 - math
    # arr = [1, 2, 4, 3, 5]
    # sum_nums = sum(arr)
    # if sum_nums % 2 != 0:
    #     return -1
    # avg = sum_nums / 2
    # num_pairs = 0
    # for num in arr:
    #     num_pairs += num - avg
    # num_pairs = int(num_pairs / 2)
    # if num_pairs == 0:
    #     return -1
    # return num_pairs - 1
    # if sum(arr) % 2 == 0:
    #     return
