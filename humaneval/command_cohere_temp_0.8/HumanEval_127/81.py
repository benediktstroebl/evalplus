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
    Determine if the length of the intersection of two closed intervals is prime
    """
    # Convert the interval pairs to dictionaries with start and end values
    interval1 = {'start': s1[0], 'end': s1[1]}
    interval2 = {'start': s2[0], 'end': s2[1]}

    # Determine if the intervals intersect at all
    if interval1['end'] < interval2['start'] or interval2['end'] < interval1['start']:
        return "NO"

    # Calculate the intersection interval from the two input intervals
    x = max(interval1['end'], interval2['end'])
    y = min(interval1['start'], interval2['start'])
    intersection_length = x - y + 1

    # Check if the intersection length is prime
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"
```

The function utilizes a primitive algorithm to determine whether a number is prime or not, which checks for divisibility by all numbers from 2 to the square root of the number. 

For the interval checking mechanism, the function first converts the interval pairs to dictionaries for easier manipulation. It then checks if the start of one interval is less than the end of the other interval, meaning there's no overlap, and returns `NO`. Otherwise, it calculates the length of the intersection and checks if this length is prime, accordingly returning `YES` or `NO`. 

Both functions comprise a standalone approach that does not rely on any external libraries or modules, adhering to the self-contained clause in the prompt. 
```