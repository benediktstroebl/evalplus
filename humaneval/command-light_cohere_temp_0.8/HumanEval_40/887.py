```python
def triples_sum_to_zero(lst):
    sum_to_zero = [0, 0, 0]
    for num in lst:
        if sum_to_zero[0] + sum_to_zero[1] + sum_to_zero[2] == 0:
            sum_to_zero[0] += num
            sum_to_zero[1] += num
            sum_to_zero[2] += num
            break
    return bool(sum_to_zero[0] == 0)

# Test the function
if __name__ == "__main__":
    print(triples_sum_to_zero([1, 3, -2, 1])))
    print(triples_sum_to_zero([1, 2, 3, 7])))
    print(triples_sum_to_zero([2, 4, -5, 3, 9, 7])))
    print(triples_sum_to_zero([1])))
```
The `triples_sum_to_zero` function will return `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise. 
The function utilizes a nested list `sum_to_zero` to keep track of the three sums, and a loop to iterate through the list.