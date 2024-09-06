
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
    even_arr = [0] * len(arr)
    odd_arr = [0] * len(arr)
    for i in range(len(arr)):
        if i % 2 == 0:
            even_arr[i] = arr[i]
        else:
            odd_arr[i] = arr[i]

    # 이거 일단 풀어봤음
    # def smallest_change(arr):
    #     arr = arr[::-1]
    #     even_arr = [0] * len(arr)
    #     odd_arr = [0] * len(arr)
    #     for i in range(len(arr)):
    #         if i % 2 == 0:
    #             even_arr[i] = arr[i]
    #         else:
    #             odd_arr[i] = arr[i]

    # 이것도 이런식으로 옮겨봄
    # def smallest_change(arr):
    #     even_
