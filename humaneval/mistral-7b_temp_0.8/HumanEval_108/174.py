
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    # Your code goes here.
    # 예제로 보여준 것 처럼 리스트 안의 원소를 하나씩 확인하여 해당 원소의 각 자리 숫자를 더해보면 된다.
    # 0은 제외한다.

    # for i in arr:
    #     print(i)
    #     if int(i) != 0:
    #         count = 0
    #         for j in str(int(i)):
    #             print(j)
    #             count += int(j)
    #         if count > 0:
    #             print(count)

    # 정답 예시
    count = 0
    for num in arr:
        num_sum = 0
        if num != 0:
            for digit in str(num):
                num_sum += int(digit)
            if num_sum > 0:
                count += 1
    return count


