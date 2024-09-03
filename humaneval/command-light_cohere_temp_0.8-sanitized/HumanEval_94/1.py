def skjkasdkd(lst):
    """
    Find the largest prime factor and return sum of its digits
    """
    list_prime = []
    for num in lst:
        if num <= 1 :
            continue
        for i in range(0, 10) :
            if int(num * 10**i) == num:
                list_prime.append(10*i)
                break
        if len(list_prime) == 1 :
            return int(list_prime[0])
        else :
            lst.reverse()