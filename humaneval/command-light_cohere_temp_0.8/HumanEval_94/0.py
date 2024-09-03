```python
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
           while len(list_prime) > 1:
                temp = list_prime[0]
                list_prime[0] = list_prime.pop(0)
                list_prime.append(int(temp))
            if len(list_prime) == 1 :
                return int(list_prime[0])
    return int(lst)
```