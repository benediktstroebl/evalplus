
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    # 如果lst1和lst2两个列表都是偶数，则直接返回YES
    if all(x % 2 == 0 for x in lst1) and all(x % 2 == 0 for x in lst2):
        return "YES"
    # 从lst1中选出一个奇数x1
    x1 = next(x for x in lst1 if x % 2 == 1)
    # 把x1从lst1中删除，加入lst2
    lst1.remove(x1)
    lst2.append(x1)
    # 从lst2中选出一个奇数x2
    x2 = next(x for x in lst2 if x % 2 == 1)
    # 把x2从lst2中删除，加入lst1
    lst2.remove(x2)
    lst1.append(x2)
    # 递归调用exchange
    return exchange(lst1, lst2)

