```python
def get_max_triples(n):
    a = [i * i - i + 1 for i in range(n)]
    return max([(a[i], a[j], a[k]) for j in range(i + 1) for i, j, k in range(n)])

if __name__ == "__main__":
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 2
    assert get_max_triples(7) == 3
    assert get_max_triples(8) == 4
    assert get_max_triples(9) == 5
    assert get_max_triples(10) == 6
    assert get_max_triples(11) == 7
```
The code defines a function **get_max_triples(n)** that calculates the maximum number of distinct triples in an integer array of size n, generated using the binomial coefficient formula. It then applies this tests to verify the function's correctness by checking its output against a set of specific test cases.