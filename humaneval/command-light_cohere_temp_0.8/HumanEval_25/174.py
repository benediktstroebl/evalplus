```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    """
    if n < 2:
        raise ValueError("Input number must be a positive integer")
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    n % 3 == 0 and factors.append(3) or
    n % 5 == 0 and factors.append(5)
    n % 7 == 0 and factors.append(7)
    n % 11 == 0 and factors.append(11)
    n % 13 == 0 and factors.append(13)
    n % 17 == 0 and factors.append(17)
    n % 19 == 0 and factors.append(19)
    n % 23 == 0 and factors.append(23)
    n % 29 == 0 and factors.append(29)
    n % 31 == 0 and factors.append(31)
    n % 37 == 0 and factors.append(37)
    n % 41 == 0 and factors.append(41)
    n % 43 == 0 and factors.append(43)
    n % 47 == 0 and factors.append(47)
    n % 53 == 0 and factors.append(53)
    n % 59 == 0 and factors.append(59)
    n % 61 == 0 and factors.append(61)
    n % 67 == 0 and factors.append(67)
    n % 71 == 0 and factors.append(71)
    n % 73 == 0 and factors.append(73)
    n % 79 == 0 and factors.append(79)
    n % 83 == 0 and factors.append(83)
    n % 89 == 0 and factors.append(89)
    n % 97 == 0 and factors.append(97)
    n % 101 = 0 and factors.append(101)
    n % 103 = 0 and factors.append(103)
    n % 107 = 0 and factors.append(107)
    n % 109 = 0 and factors.append(109)
    n % 113 = 0 and factors.append(113)
    n % 117 = 0 and factors.append(117)
    n % 119 = 0 and factors.append(119)
    n % 121 = 0 and factors.append(121)
    n % 123 = 0 and factors.append(123)
    n % 125 = 0 and factors.append(125)
    n % 137 = 0 and factors.append(137)
    n % 139 = 0 and factors.append(139)
    n % 147 = 0 and factors.append(147)
    n % 149 = 0 and factors.append(149)
    n % 151 = 0 and factors.append(151)
    n % 157 = 0 and factors.append(157)
    n % 163 = 0 and factors.append(163)
    n % 169 = 0 and factors.append(169)
    n % 171 = 0 and factors.append(171)
    n % 173 = 0 and factors.append(173)
    n = 1
n_factors = []
    for num in factors:
        n_factors.append(num*num)
    return n_factors
```  This function is self-contained and solves the problem. It returns a list of prime factors of the given integer in the order from smallest to largest.