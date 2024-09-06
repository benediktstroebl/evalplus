```python
def tri(n):
    result = [0, 1, 3]
    while len(result) < n + 1:
        num = 1 if result[-1] % 2 == 0 else 0
        result.append(result[-1] + result[-2] + result[-3] + num)
    return result[:n+1]
``` 

This code defines a function called `tri` that takes a parameter `n`, which represents the desired length of the Tribonacci sequence. The function starts by initializing a mini sequence of the first three Tribonacci numbers(0, 1, 3), it then enters a loop that keeps adding numbers to the sequence until its length is greater than `n`. Within the loop, it decides whether to add 1 to the current number based on the parity of the previous number, it then adds the current number to the growing sequence. The output is a list containing the first `n` numbers of the Tribonacci sequence.