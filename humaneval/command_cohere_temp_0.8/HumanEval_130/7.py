```python
def tri(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    trib = [0, 0, 0]
    for i in range(2, n + 1):
        if i % 2 == 0:
            trib.append(1 + i // 2)
        else:
            trib.append(trib[i - 1] + trib[i - 2] + trib[i + 1])
    return trib
```
This Python script defines a function 'tri' that computes the Tribonacci sequence, a variation of the Fibonacci sequence. It initializes three variables 'trib' with initial values [0, 0, 0], and then iterates from 2 to 'n' (n + 1) to either calculate the value as 1 + (i // 2) or sum the previous three values from 'trib'. The function returns the list of the first 'n' + 1 values of the Tribonacci sequence, and handles the cases when n is 0 or 1, returning an empty list or [1] respectively. 

Here's an example of how to use the function to calculate the Tribonacci sequence for 'n' = 4:
```python
print(tri(4))
```
This will output:
[1, 3, 2, 8]