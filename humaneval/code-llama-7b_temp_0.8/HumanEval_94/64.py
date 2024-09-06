

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """

    lst = sorted(lst)
    new_lst = lst[::-1]
    # print(new_lst)
    lst2 = []
    lst3 = []
    for i in range(len(new_lst)):
        if i == 0:
            lst2.append(new_lst[i])
        else:
            if new_lst[i] == new_lst[i - 1]:
                continue
            else:
                lst2.append(new_lst[i])

    # print(lst2)
    for i in range(len(lst2)):
        if i == 0:
            lst3.append(lst2[i])
        else:
            if lst2[i] < lst2[i - 1]:
                continue
            else:
                lst3.append(lst2[i])

    # print(lst3)
    lst4 = lst3[::-1]

    for i in range(len(lst4)):
        if i == 0:
            if lst4[i] % 2 == 0:
                lst4[i] += 1
                break
            else:
                continue
        else:
            if lst4[i] % 2 == 0 and lst4[i - 1] % 2 == 0:
                lst4[i] += 1
                break
            elif lst4[i] % 2 == 0 and lst4[i - 1] % 2 != 0:
                lst4[i] += 1
                break
            else:
                continue

    print(lst4)
    for i in range(len(lst4)):
        if i == 0:
            continue
        else:
            if lst4[i] < lst4[i - 1]:
                lst4.remove(lst4[i])
                lst4.insert(i, lst4[i - 1])
    print(lst4)

    for i in lst4:
        if i < 10:
            lst4.remove(i)

    print(lst4)

    for i in range(len(lst4)):
        if
