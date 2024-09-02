
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n % 10 == 1:
        return (n // 10) + starts_one_ends(n//10)
    else:
        count = 0
        for i in range(1, n // 2):
            count += starts_one_ends(n - i * 10)
        count += starts_one_ends(n // 10)
        return count

print(starts_one_ends(100)) # 4
print(starts_one_ends(1000)) # 20
print(starts_one_ends(10000)) # 100
\end{code}

Here is the benchmark of the above solutions using `nose` and `timer` modules.

\begin{code}
import numpy as np
from nose.tools import *
import timer
