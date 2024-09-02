
def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """
    # This is a basic Python program to test if two given integers are prime numbers.
    # This program uses a simple trial division method to test if the number is prime or not.
    def isPrime(x):
        if x == 2:
            return True
        if x % 2 == 0 or x < 2:
            return False
        for i in range(3, int(x**0.5)+1, 2):
            if x % i == 0:
                return False
        return True
    a,b,c,d=interval1
    a1,b1,c1,d1=interval2
    #print(a,b,c,d)
    #print(a1,b1,c1,d1)
    if a>=c1 and b>=d1:
        return 'YES'
    elif b<=c1 and a<=d1:
        return 'YES'
    elif a>=c and b>=d:
        return 'YES'
    elif b<=c and a<=d:
        return 'YES'
