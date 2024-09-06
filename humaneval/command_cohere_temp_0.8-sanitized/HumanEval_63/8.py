def fibfib(n):
    fibfib_sequence, prev_val, curr_val = [0, 0, 1], 0, 0
    while len(fibfib_sequence) < n:
        prev_val = curr_val
        curr_val = fibfib_sequence[-1] + prev_val + fibfib_sequence[-2]
        fibfib_sequence.append(curr_val)
    return curr_val