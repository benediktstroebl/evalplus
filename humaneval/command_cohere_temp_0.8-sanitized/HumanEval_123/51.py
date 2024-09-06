def get_odd_collatz(n):
    seq = [1]
    if n > 1:
        seq += [n]
        odd = n % 2
        while len(seq) < 1000 :    
            if seq[-1] % 2 == 0:
                seq += [seq[-1] // 2]
            else:
                seq += [3 * seq[-1] + 1]
            if seq[-1] == 1:
                break
    return [num for num in seq if num % 2 != 0]