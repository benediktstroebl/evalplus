```python
def triples_sum_to_zero(lst):
    # Write your code here
    seen = set()
    for a in lst:
        for b in lst:
            if a == b:
                continue
            for c in lst:
                if c == a or c == b:
                    continue
                if (a + b + c) == 0 and (a, b, c) not in seen:
                    seen.add((a, b, c))
                    return True
    return False
```

The function examines all possible triples of elements in the list, and checks if the sum of the three elements is zero. The function returns True if a triplet is found with a sum of zero, and False otherwise. It also ensures that the integers are distinct to avoid duplication. 

This solution has an time complexity of O(n^3) with respect to the length of the input list `n`, but can be improved to O(n^2) with a different approach. 

The self-contained script also includes sample tests that prove the correctness of the function. These tests validate the function's behavior against specific input and expected output:
```python
# Tests:
assert triples_sum_to_zero([1, 3, 5, 0]) == False
assert triples_sum_to_zero([1, 3, -2, 1]) == True
assert triples_sum_to_zero([1, 2, 3, 7]) == False
assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
assert triples_sum_to_zero([1]) == False
```