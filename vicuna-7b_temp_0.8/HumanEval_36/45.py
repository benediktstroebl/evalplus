

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    stack = []
    result = []
    for i in range(n):
        if i % 11 == 0:
            stack.append(i)
        elif i % 13 == 0:
            result.append(i)
        else:
            while stack and stack[-1] == 0:
                stack.pop()
            while stack and stack[-1] == 1:
                stack.pop()
            if len(stack) > 0:
                stack[-1] *= 7
                stack.pop()
        if i % 11 == 0:
            result.append(stack[-2] + stack[-1])
        elif i % 13 == 0:
            result.append(stack[-1])
    return result
