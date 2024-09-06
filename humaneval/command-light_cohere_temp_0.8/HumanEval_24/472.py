```python
def largest_divisor(n: int) -> int:
    return n // max(x for x in range(1, n+1) if x % n == 0)
``` 
This function uses the concept of the greatest factor, where it returns the largest number which divides the number evenly. It uses a process similar to find the largest divisor, which is to find the largest number that divides the number evenly, by checking divisibility from largest numbers up to the given number.