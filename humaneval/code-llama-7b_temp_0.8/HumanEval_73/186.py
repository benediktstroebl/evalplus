
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
    # O(NlogN)
    # arr.sort()
    # return len(arr) - next((i for i in range(len(arr) // 2, -1, -1) if arr[i] != arr[len(arr) - 1 - i]))
    
    # O(N^2)
    # total_change = 0
    # for i in range(len(arr) // 2):
    #     for j in range(i + 1, len(arr) - i):
    #         total_change += abs(arr[i] - arr[j])
    # return total_change

    # O(N)
    # total_change = 0
    # value_dict = {}
    # for i in range(len(arr) // 2):
    #     value_dict[arr[i]] = value_dict.get(arr[i], 0) + 1

    # for i in range(len(arr) // 2, len(arr)):
    #     value = arr[i]
    #     if value_dict.get(value, 0) == 0:
    #         total_change += 1
    #     else:
    #         value_dict[value] -= 1
    #         total_change += (1 if value_dict.get(value) < 0 else 0)
    # return total_change

    # O(N)
    # total_change = 0
    # value_dict = {}
    # for i in range(len(arr) // 2):
    #     value = arr[i]
    #     value_dict[value] = value_dict.get(value, 0) + 1

    # for i in range(len(arr) // 2, len(arr)):
    #     value = arr[i]
    #     if value_dict.get(value, 0) == 0:
    #         total_change += 1
    #     else:
    #         value_dict[value] -= 1
    #         total_change += (1 if value_dict.get(value) < 0 else 0)
