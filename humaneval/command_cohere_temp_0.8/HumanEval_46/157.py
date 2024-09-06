```python
def fib4(n: int) -> int:
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    return fib4_list[n]
```
This script uses an iterative approach to calculate the Fib4 number sequence and achieves a time complexity of O(n) for calculating the nth Fib4 number. 

And here is a more detailed explanation of how it works:
1. The function `fib4` takes an integer `n` as input, representing the position of the number we want to calculate in the Fib4 sequence.
2. An initial list `fib4_list` is defined with the first five elements of the Fib4 sequence (0, 0, 2, 0, 0). These are the basis for the iterative calculation.
3. A loop iterates over the indices `i` from 5 to `n`, which represents the range of elements in the Fib4 sequence that have been calculated.
4. For each iteration, the next element in the sequence is calculated as the sum of the last four elements in the list. This is the defining characteristic of the Fib4 sequence.
5. Each calculated element is appended to the `fib4_list`, ensuring that the list contains the entire Fib4 sequence up to the nth number.
6. After the loop completes, the `fib4_list` contains the calculated Fib4 number for the position `n`.
7. The function returns the value of `fib4_list[n]`, which is the nth element of the Fib4 sequence.

This approach ensures that each element in the sequence is calculated only once, making it efficient and avoiding the recursive complexity of the naive recursive approach.