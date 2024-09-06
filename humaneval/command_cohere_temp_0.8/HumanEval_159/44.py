Here's a Python script that contains a function named `eat` which solves the given problem:
```python
def eat(n, need, rem):
    ans = [n + need, min(need, rem)]
    if ans[1] == need:
        return ans
    else:
        return [ans[0], 0]
```
This function calculates the total number of carrots consumed during meals and the number of carrots left after the meals in the life of a rabbit. It works with the following steps:
1. The function takes in three variables: `n` which represents the number of carrots already eaten, `need` which represents the target number of carrots to eat, and `rem` which represents the remaining quantity of carrots available.
2. It initializes an array `ans` with two elements: `n + need` and `min(need, rem)`. The first element represents the total number of carrots consumed after eating the desired amount, and the second element represents the number of carrots left after eating. 
3. The function returns the `ans` array if the number of carrots left (`ans[1]`) is equal to the needed amount after eating (`need`). If the rabbit has eaten enough to be satisfied, it will return the array with the total carrots eaten and the remaining carrots.
4. If the number of carrots left (`ans[1]`) is less than the desired amount to eat (`need`), it returns `[ans[0], 0]` because the rabbit will eat all the remaining carrots but still be hungry afterward since it did not eat enough.

Note: This scenario assumes that the rabbit can eat exactly one carrot per meal, and the behavior of the function is tailored to this assumption. You can customize it according to different rules if needed.