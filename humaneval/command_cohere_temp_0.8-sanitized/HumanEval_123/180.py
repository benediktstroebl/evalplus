def get_odd_collatz(n):
    odd_collatz = [1]
    while n != 1: 
        if len(odd_collatz) == 0:
            odd_collatz.append(n)
        elif odd_collatz[-1] == 1:
            odd_collatz.append(n)
        else:
            odd_collatz.append(3*n + 1)
        n = odd_collatz.pop()
    return odd_collatz