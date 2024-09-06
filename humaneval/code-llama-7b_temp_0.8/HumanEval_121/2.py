
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    return sum([e for i,e in enumerate(lst) if i % 2 == 0 and e % 2 != 0])



    # itertools.starmap()
    # def func(a,b):
    #     return a + b

    # def func1(a,b):
    #     return a - b

    # def func2(a,b):
    #     return a * b

    # def func3(a,b):
    #     return a / b

    # a = [5, 8, 7, 1]
    # b = [1, 2, 3, 4]
    # # map(lambda x: x+y, a,b)
    # # map(lambda x: x*y, a,b)
    # # map(lambda x: x-y, a,b)
    # # map(lambda x: x/y, a,b)

    # # func2(a,b)
    # # func3(a,b)

    # # starmap(lambda x,y:x+y, zip(a,b))
    # # starmap(lambda x,y:x-y, zip(a,b))
    # # starmap(lambda x,y:x*y, zip(a,b))
    # # starmap(lambda x,y:x/y, zip(a,b))

    # # map(lambda x: func(x[0],x[1]), zip(a,b))
    # # map(lambda x: func1(x[0],x[1]), zip(a,b))
    # # map(lambda x: func2(x[0],x[1]), zip(a,b))
    # # map(lambda x: func3(x[0],x[1]), zip(a,b))

    # print(func2(a,b))

    # a = [1,2,3,4,5]
    # print(list(filter(lambda x: x%2==0, a)))

    # a = [1,2,3,4,5,6,7,8
