

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    "*** YOUR CODE HERE ***"
    nums = [str(i) for i in range(1, n+1)]
    for num in nums:
        if num.count('7') > 0 and (num.count('1') > 0 or num.count('2') > 0 or num.count('3') > 0):
            continue
        if num.count('1') > 0 and num.count('3') > 0:
            num = int(num)
            if num % 11 == 0 or num % 13 == 0:
                continue
        if num.count('2') > 0 and num.count('3') > 0:
            num = int(num)
            if num % 13 == 0 or num % 11 == 0:
                continue
        print(num)
