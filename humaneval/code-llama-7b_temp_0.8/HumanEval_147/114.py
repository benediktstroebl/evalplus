
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    # your code here
    # 1 3 7 13 21
    # 1^2 = 1
    # 1+3 = 4 => 4 is multiple of 3
    # 1^2 + 3^2 = 4 + 9 = 13
    # 1 + 7 + 13 = 21
    # 7 + 13 + 21 = 40
    # 1^2 + 7^2 + 13^2 = 4+49+169
    # 7+13+21 = 40
    # 1+7+13+21 = 55
    # 55/3 = 18.66667
    # 18 = 18*3
    # 55/3 = 18.66667
    # 55/3 = 18.66667*3
    # 18.66667 is not a whole number
    # 55/3 = 18.66667*3 = 2
    # 55/3 = 18.66667*3 = 2.333333
    # 2.333333*3 = 7
    # 2.333333*3 = 7.666666
    # 7.666666*3 = 23.999999
    # 7.666666*3 = 23.999999*3
    # 23.999999*3 = 73
    # 23.999999*3 = 73.666666
    # 23.999999*3 = 73.666666*3
    # 73.666666*3 = 230
    # 73.666666*3 = 230.6666
