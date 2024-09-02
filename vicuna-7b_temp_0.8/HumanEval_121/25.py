
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # 遍歷列表，每次遍历前面是否有奇数元素
    for i in range(len(lst)-1):
        if lst[i] % 2 != 0:
            return lst[i]
    return 0

def main():
    # 创建输入流，读取列表
    inp = input()
    lst = list(map(int, inp.split()))

    # 执行解决方案
    s = solution(lst)

    # 输出结果
    if s == 0:
        print("无解")
    else:
        print(s)

if __name__ == "__main__":
    main()