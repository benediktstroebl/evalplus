
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # your code here

    # num = str(num)
    # print(num)
    # even = []
    # odd = []
    # for i in num:
    #     if int(i) % 2 == 0:
    #         even.append(int(i))
    #     else:
    #         odd.append(int(i))
    # # print(even)
    # # print(odd)
    # return len(even), len(odd)
    # 1. 如果要做到类似 12 这种输出呢
    # （1，2）
    #   >>> print('(' + str(len([x for x in map(int, str(num)) if x % 2 == 0])) + ',' + str(len([x for x in map(int, str(num)) if x % 2 != 0])) + ')')
    # （2，1）
    # 2. 如果要输出的格式不同呢
    # ('1', '2')
    # （2，1）
    # 3. 如果要输出的格式不同呢
    # [1, 2]
    # [2, 1]
    # print('(' + str(len([x for x in map(int, str(num)) if x % 2 == 0])) + ',' + str(len([x for x in map(int, str(num)) if x % 2 != 0])) + ')')
    #
    # 4. 如果要输出的格式不同呢
    # ('1', '2')
    # ('2', '1')
    # print(str(tuple([x for x in map(int, str(num)) if x % 2 == 0])))
    # print(str(tuple([x for x in map(int, str(num)) if x % 2 != 0])))

    count_even = sum(1 for i in str(num) if int(i) % 2 == 0)
    count_odd = len(str(num
