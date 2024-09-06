
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
    # Your code here
    # 이 함수는 두 개의 숫자 리스트를 받아 하나의 리스트에는 짝수의 숫자들로 이루어져
    # 있을 때 다른 리스트에서 숫자들을 교환하여 짝수로만 이루어진 리스트를 만들 수 있는지
    # 확인하는 함수이다. 교환하는 횟수에 제한은 없다.
    # 교환을 통해 짝수가 모두 되는 경우는 "YES" 를 리턴하고, 그 외의 경우에는 "NO"를 리턴한다.
    # 이 함수에는 어떠한 제한도 없다.
    for index, number in enumerate(lst1):
        if number % 2 == 1:
            for x, num in enumerate(lst2):
                if num % 2 == 0:
                    lst1[index] = num
                    lst2[x] = number
                    return "YES"
    return "NO"
