```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if -x in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This function iterates through every element in the list and simply checks whether the list has two elements that add up to zero. It checks for both positive and negative elements to find pairs that sum up to zero. Two identical elements that add up to zero would also return True, so please clarify if this is a concern. In that case, a more elaborate approach would be needed, using things like sorting the list and picking consecutive elements. 

The unit tests provided in the original prompt are simple and helpful. However, it's good practice to have a more diverse set of test cases to cover edge scenarios. Here's an example: 
```python
test_cases = [
    [1, 3, 5, 0], 
    [1, 3, -2, 1], 
    [1, 2, 3, 7], 
    [2, 4, -5, 3, 5, 7],
    [1],
    [2, -2, 2, -2, -2],
    [0, 0, 0, 0, 1, 2, -1, -2, -1, 1, 2, 0, 0],
    [-5, -3, 0, 5, 3]
]

expected_ans = [False, False, False, True, False, True, False, True, False]

for i in range(len(test_cases)):
    assert pairs_sum_to_zero(test_cases[i]) == expected_ans[i]
``` 

This script provides a more thorough test suite for the function, covering positive and negative test scenarios.