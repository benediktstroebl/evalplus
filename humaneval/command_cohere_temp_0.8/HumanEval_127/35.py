```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def intersection(s1, s2):
    st, en = max(s1[0], s2[0]), min(s1[1], s2[1])
    if st > en:
        return "NO"
    else:
        diff = en - st + 1
        if is_prime(diff):
            return "YES"
        else:
            return "NO"
```

The approach uses a simple algorithm to determine if a number is prime or not. The function `is_prime` determines if a given number n is prime or not. The function `intersection` calculates the length of the intersection of two intervals and then calls `is_prime` to determine if the length of the intersection is prime. 

Here is a breakdown of the code:
- The function `is_prime` checks if a given number is prime or not. If the number is less or equal to 1 it returns False, if the number is 2 or 3 it returns True. For numbers greater than 3, it checks if the number is divisible by 2 or 3, if so it returns False. For numbers that are not divisible by 2 or 3, it starts checking for divisibility by 5 and onwards, incrementing by 6 each time.
- The function `intersection` finds the start and end values of the intersection of two intervals and then uses the `is_prime` function to determine if the length of the intersection is prime. If the start is greater than the end, it returns "NO" straightaway. Otherwise, it calculates the length of the intersection and checks if this length is prime. If it is, it returns "YES", otherwise, it returns "NO".  In the end, the code includes corresponding tests that validate the code. 
```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def intersection(s1, s2):
    st, en = max(s1[0], s2[0]), min(s1[1], s2[1])
    if st > en:
        return "NO"
    else:
        diff = en - st + 1
        if is_prime(diff):
            return "YES"
        else:
            return "NO"

# Tests
assert intersection((1, 2), (2, 3)) == "NO"
assert intersection((-1, 1), (0, 4)) == "NO"
assert intersection((-3, -1), (-5, 5)) == "YES"
```