
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    odd_lst = []
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            odd_lst.append(lst[i])
    return sum(odd_lst)

if __name__ == '__main__':
    t = len(lst) // 2
    num = 0
    for i in range(t):
        num += solution(lst[i*2:(i+1)*2])
    print(num)