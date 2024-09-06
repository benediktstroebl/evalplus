```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Determine whether the length of intersection of two given closed intervals is a prime number.
    """
    # Convert interval to tuple (start, end)
    x = (max(s1[0], s2[0]), min(s1[1], s2[1]))
    # Check if the two intervals intersect
    if x[0] >= x[1]:
        return "NO"
    else:
        # Calculate the length of the intersection and check if it's prime
        length = x[1] - x[0] + 1
        if is_prime(length):
            return "YES"
        else:
            return "NO"
```

The approach used by the function `intersection()` is discussed below:
1. Convert Intervals to Integers: The function converts the two given intervals to integers (start, end) and calculates the length of the intersection.
2. Check for Intersection: The function checks if the start index is less than the end index. If they are not in the correct order or if they are equal, then there is no intersection and the function returns "NO."
3. Check Prime: The function calculates the length of the intersection and checks if it's a prime number using the `is_prime()` function. If the length is prime, it returns "YES." Otherwise, it returns "NO." 

The `is_prime()` function is a simple and efficient way to check if a number is prime. The range of the loop is limited to int(n**0.5)+1 to avoid the overflow possibility of the counter and int(n**0.5) is calculated to be the sqrt(n) to optimize the loop.

Overall, the code is efficient and can solve the problem in O(log(n)) time where n is the length of the intersection of the intervals.