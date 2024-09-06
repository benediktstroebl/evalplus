from collections import Counter
def fibfib_naive(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib_naive(n - 1) + fibfib_naive(n - 2) + fibfib_naive(n - 3)
def fibfib(n: int):
    if n < 3:
        return n
    else:
        # Use the Counter to keep track of values and compute them efficiently
        fibfib_counter = Counter(range(n))
        return fibfib_counter[fibfib_naive(n - 1)] + fibfib_counter[fibfib_naive(n - 2)] + fibfib_counter[fibfib_naive(n - 3)]