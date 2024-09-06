```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The algorithm works by recursive elimination of the larger value from the pair of integers, until the 'b' value becomes zero. At that point, the 'a' value is the greatest common divisor of the original pair 'a' and 'b'. 

This GCD algorithm is called the Euclidean algorithm. It is named after the Greek mathematician Euclid, who first published it in his book Elements around 300 BC.