
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if n > m:
        return -1
    if n == m:
        return f'0b{bin(n)[2:]}'.rjust(8, '0')
    arr = [x for x in range(n, m+1)]
    print(arr)
    arr_sum = sum(arr)
    print(arr_sum)
    if len(arr) % 2 == 0:
        avg = arr_sum / len(arr)
        print(avg)
        avg_round = round(avg)
        print(avg_round)
        return f'0b{bin(avg_round)[2:]}'.rjust(8, '0')
    else:
        avg = arr_sum / len(arr)
        print(avg)
        avg_round = round(avg)
        avg_round_up = avg_round + 1
        print(avg_round)
        print(avg_round_up)
        return f'0b{bin(avg_round_up)[2:]}'.rjust(8, '0')
