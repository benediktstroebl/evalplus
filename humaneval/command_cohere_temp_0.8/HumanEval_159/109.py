Here's a Python script that contains a function eat() that solves the given problem:
```python
def eat(n, need, rem):
    ans = [n + need, min(need, rem)]
    if ans[1] < need:
        ans[0] = ans[0] + (need - ans[1])
    return ans
```
This script defines a function eat which takes in three variables, n (number of carrots already eaten), need (number of carrots needed to be eaten), and rem (the number of remaining carrots). The answer is returned as a list [n + need, min(need, rem)], where the second value is assigned the minimum of needing carrots and the remaining carrots to be eaten. In case there are not enough remaining carrots to fulfill the need, the first value in the list is increased by the difference between the needed carrots and the remaining carrots. To be certain our function works correctly we can test it using the following code:
```python
def test_eat():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]
    assert eat(0, 1, 1) == [1, 0]
    assert eat(1000, 1, 2) == [1, 1]
```
This code provides multiple assertions that test the function with different use cases to ensure its correctness.