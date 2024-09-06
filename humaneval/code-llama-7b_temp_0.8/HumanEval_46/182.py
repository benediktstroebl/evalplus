

def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    # Your code here
    # we can use iteration instead of recursion
    # 1. create a list that stores the elements of the fib4 sequence
    # 2. initialize it with 0,0,2,0
    # 3. start iterating
    # 4. get the last four elements
    # 5. add them up
    # 6. append the result to the end of the list
    # 7. return the last element of the list
    # time complexity is O(n)
    # space complexity is O(1)
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0
    fib_list = [0, 0, 2, 0]
    for i in range(4, n + 1):
        last_four_elements = fib_list[-4:]
        result = sum(last_four_elements)
        fib_list.append(result)
    return fib_list[-1]

