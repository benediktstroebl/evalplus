
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
    from collections import defaultdict
    d = defaultdict(int)
    for num in arr:
        d[num] += 1
    print(d)
    answer = 0
    even = 0
    odd = 0
    for num in d.keys():
        print(num)
        if num % 2 == 0 and d[num] % 2 == 1:
            answer += (d[num] - 1)
        elif num % 2 == 0:
            answer += d[num]
        if d[num] % 2 == 1:
            odd += 1
        if d[num] % 2 == 1 and odd % 2 == 0:
            answer -= 1
        else:
            even += 1
        if d[num] % 2 == 0 and even % 2 == 1:
            answer += 1
    return answer
