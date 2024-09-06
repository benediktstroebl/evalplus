```python
def starts_one_ends(n):
    pos_ints = [str(i) for i in range(1, n + 1)]
    pos_ints_starting_with_1 = [i for i in pos_ints if i[0] == '1']
    pos_ints_ending_with_1 = [i for i in pos_ints if i[-1] == '1']
    
    return len(pos_ints_starting_with_1) + len(pos_ints_ending_with_1)
```

This function uses two list comprehensions to generate `pos_ints_starting_with_1` and `pos_ints_ending_with_1`, which are the integers within the prescribed range that start or end with 1, respectively. The sum of the lengths of these two lists is then returned, giving the total count of desired numbers. 

You can ensure the function's correctness by comparing it with the results of the given tests, as the test cases essentially provide the ground truth for the problem. Let's verify the function's behavior by incorporating these tests into the code:
```python
# Testing the function with various input values
n = 5
expected_result = 8

assert starts_one_ends(n) == expected_result
print("Test passed.")
```

You can adjust the value of `n` and the expected result in accordance with your test cases.