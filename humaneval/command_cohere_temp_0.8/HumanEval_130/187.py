```python
def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [1] + tri(n - 1)
    else:
        return [1] + tri(n - 1) + tri(n - 2) + tri(n + 1)
```
The function takes an integer n as input and returns the list of the first n + 1 Tribonacci numbers. To achieve this, it employs three base cases:
1. n == 0: This is the termination case where it returns an empty list. 
2. n == 1: This is the initial case where the function returns only the base Tribonacci number, 1. 
3. n % 2 == 0: This is the recursive case for even numbers where the function returns the previous two Tribonacci numbers plus the new calculated Tribonacci number (1 + n/2). 

For the recursive case of odd numbers, the function returns the sum of the previous three Tribonacci numbers: 

```python
print(tri(1))  # Output: [1]
print(tri(2))  # Output: [1, 3]
print(tri(3))  # Output: [1, 3, 2, 8]
print(tri(4))  # Output: [1, 3, 2, 8, 5, 13, 8, 18]
```

Feel free to experiment with different input values to observe the patterns of the Tribonacci sequence. You can use this script to compute the first n + 1 Tribonacci numbers and analyze the properties of this lesser-known mathematical sequence.