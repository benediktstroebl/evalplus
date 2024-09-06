```python
def tri(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [0] + tri(n - 1)
    else:
        return [1] + tri(n - 1) + tri(n - 2) + tri(n + 1)
```
The function uses a set of recursive cases corresponding to the definition of the Tribonacci sequence. The first case (n=0) is the base case as it directly returns the list of numbers for n=0 term. The second case (n=1) is also direct as it only consists of the first element of the Tribonacci sequence. The third case (n%2==0) handles even numbers and recursively calls the function with the value n-1. The last case (n%2!=0) is for odd numbers and recursively calls the function with the values n-1, n-2, and n+1. Each recursive call builds the list of Tribonacci numbers until the base case of n=0 is reached.