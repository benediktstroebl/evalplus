Here's a Python script that contains a function eat() that solves the given problem:
```python
def eat(n, need, rem):
    return [n + min(need, rem), max(0, rem - need)]
```
This function takes three parameters, n (number of carrots already eaten), need (number of carrots needed to eat), and rem (the number of remaining carrots). The function returns a list containing two integers: the total number of carrots eaten after meals and the number of carrots left after meals.

The logic is to add the number of already eaten carrots to the minimum of the number of carrots needed to eat and the remaining carrots. This ensures that the rabbit eats as many carrots as needed and minimizes the number of carrots eaten in case there is a shortage. The second value in the returned list is the result of taking the maximum of zero and the difference between the remaining carrots and the number of carrots needed to eat. This means that if there are not enough carrots to fill the gap, the rabbit will eat all the remaining carrots, but will still be hungry.