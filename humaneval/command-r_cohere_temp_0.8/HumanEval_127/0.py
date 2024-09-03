```python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """Determine if the length of the intersection is a prime number"""
    start1, end1 = interval1
    start2, end2 = interval2

    # Check if the intervals intersect
    if end1 < start2 or end2 < start1:
        return "NO"
    
    # Find the length of the intersection
    intersect_start = max(start1, start2)
    intersect_end = min(end1, end2)

    length = intersect_end - intersect_start + 1

    return "YES" if is_prime(length) else "NO"

# Test cases
assert intersection((1, 2), (2, 3)) == "NO"
assert intersection((-1, 1), (0, 4)) == "NO"
assert intersection((-3, -1), (-5, 5)) == "YES"
```