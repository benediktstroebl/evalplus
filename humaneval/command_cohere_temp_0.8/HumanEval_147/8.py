```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    # Calculate the maximum number of triples using a counter
    counter = 0
    for i in range(n - 2):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == arr[j] + arr[j + 1]:
                counter += 1
    return counter
```
The solution uses a nested loop to create all possible pairs of neighboring elements in the array `arr`. If the sum of two neighboring elements is equal to the sum of the next element, then they form a triple that satisfies the condition. We then increment the counter `counter`.

To analyze the solution's time complexity, let's break it down:
The outer loop iterates `n - 2` times. For each iteration of the outer loop, the inner loop iterates `n - 1 - i` times. Here, `i` is the current iteration of the outer loop. For example, for the first iteration of the outer loop, the inner loop will iterate `n - 1` times. For the second iteration of the outer loop, the inner loop will iterate `n - 2` times, and so on.

Therefore, the overall time complexity can be expressed as: 
`**(n - 2) * (n - 1 - i) + constant**

For the purpose of simplification, we can express this as:
`**(n - 2) * (n - 1) / 2 + constant**

This is because the inner loop iterates half the number of times for each progressive iteration of the outer loop.

The time complexity is O(n^2) as indicated. This is a quadratic time complexity, meaning the runtime grows quadratically in relation to the input size `n`. This is the optimal solution for the given problem with the given constraints.

The constant factors in the time complexity are negligible and do not impact the overall complexity. Therefore, we do not need to consider them for this problem.  This is a common practice when analyzing algorithms and problems in tech interviews. 

Note: the above response comprises an efficient solution to the problem. Evaluating the number of feasible triples separately triples, as depicted in the original problem statement, is not the most efficient approach.