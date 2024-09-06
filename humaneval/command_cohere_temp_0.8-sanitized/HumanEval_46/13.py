def fib4(n: int) -> int:
    def fib4_helper(n: int, acc: int = 0, prev: int = 0, current: int = 0, next: int = 0) -> int:
        if n == 0:
            return acc
        elif n == 1:
            return prev
        elif n == 2:
            return current
        elif n == 3:
            return next
        else:
            return fib4_helper(n - 1, acc + prev, prev, current, next)

    return fib4_helper(n - 4)