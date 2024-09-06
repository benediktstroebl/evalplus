```python
def fib4(n: int) -> int:
    fib4_list = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])
    return fib4_list[n]
```

This code defines a list `fib4_list` that represents the first 5 elements of the Fib4 sequence. It then uses a loop to calculate the subsequent elements in the sequence by summing the previous 4 elements in the list, and appends each new calculated element to the list. Finally, it returns the n-th element of the sequence, which is the last element in the list if n is greater than or equal to 5. 

The solution works as follows:
1. The function defines a list `fib4_list` that stores the first 5 elements of the Fib4 sequence: `0, 0, 2, 0`. These elements are defined by the base cases and the structure of the Fib4 sequence, which is similar to the Fibonacci sequence but with 4 elements at each recursive level. 
2. Then, it iterates using a loop from 5 to n, where n is the input value for which we want to compute the Fib4 number. 
3. Inside the loop, for each iteration (which corresponds to taking the 4th power of the Fib4 sequence), it calculates the next element by summing the previous 4 elements in the list using the line `fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])`. This updates the current element in the list, ensuring it captures the next element in the sequence. 
4. After the loop completes, the `fib4_list` will contain the first 5 elements followed by additional elements computed based on the recurrence relation of the Fib4 sequence. 
5. The function then returns the n-th element of the list, which represents the n-th element in the Fib4 sequence. 

This solution does not use recursion and is efficient because it calculates the elements iteratively only once up to n, resulting in a time complexity of O(n). Each element after the first 5 only requires summing 4 previous elements, so the computation is efficient.