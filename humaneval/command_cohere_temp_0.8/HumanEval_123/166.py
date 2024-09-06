```python
def get_odd_collatz(n):
    odd_seq = [x for x in collatz_seq(n) if x % 2 == 1]
    odd_seq.sort()
    return odd_seq
    
def collatz_seq(n):
    if n == 1:
        return [1]
    else:
        seq = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            seq.append(n)
        return seq
```

The `collatz_seq` function generates the sequence and the `get_odd_collatz` function then extracts the odd numbers from the sequence and returns them in a sorted fashion. 

This code should work for any input number `n` and follows the specification you provided. Let's break down the solution:
- The `collatz_seq` function is a recursive function that generates the Collatz sequence. If `n` is 1, it directly returns `[1]` since Collatz(1) is [1]. If `n` is even, it divides `n` by 2, otherwise it computes `3*n+1`, and adds the new number to the sequence. The loop continues until `n` becomes 1, which is the base case for the recursive function.
- The `get_odd_collatz` function is pretty straightforward, it is a recursive function that generates the odd numbers in the Collatz sequence, and it sorts them as stipulated in the prompt. 

This solution is clean and efficient, and should work for any input `n`.