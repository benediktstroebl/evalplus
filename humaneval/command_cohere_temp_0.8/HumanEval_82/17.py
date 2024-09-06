```python
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_length(string):
    string = str(sum(map(ord, string)))
    # converting the sum to string to make sure the
    # sum of same strings with different case will be
    # the same (e.g. SUM('ABC') == 51 and sum('abc') == 51)
    return is_prime(int(string))
```

This script defines a function `prime_length` that takes a string and converts it to a numeric value summed over its ASCII value. It then uses a fast prime-checking algorithm on that number to determine if the length of the string is prime. This approach avoids some of the problems with checking each individual character and makes the prime checking more efficient.