def fib4(n: int) -> int:
    def fib4_helper(n: int, acc: int = 0, prev: int = 0, curr: int = 0, next: int = 0) -> int:
        if n == 0:
            return acc
        if n == 1:
            return prev
        if n == 2:
            return curr
        if n == 3:
            return next
        return fib4_helper(n - 1, acc + prev, prev, curr, next)

    if n < 4:
        return n
    else:
        return fib4_helper(n - 4)