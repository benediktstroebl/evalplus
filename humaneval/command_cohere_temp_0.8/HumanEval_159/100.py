Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    cath_meal = min(n + need, rem)
    full = n + cath_meal
    return [full, rem - cath_meal]
```

This function takes in three variables `n`, `need`, and `rem` which represent the number of carrots already eaten, the number of carrots needed to be eaten, and the number of carrots remaining respectively. The function returns an array of length 2, the first element of the array is the total number of carrots eaten whereas the second element is the number of carrots remaining after the rabbit has eaten.

The function uses a min function to ensure that the rabbit will only eat the minimal required number of carrots to satisfy its hunger, to prevent overindulging. It also ensures that the number of carrots consumed cannot exceed the remaining supply. 

If the remaining supply is less than the number of carrots needed, the rabbit will eat all remaining carrots, but will still be hungry and therefore unable to satisfy its hunger. This is reflected in the returned value where the second element of the array will be 0, indicating no carrots remaining but the total amount of eaten carrots. 

For example, if passed the arguments of 5, 6, and 10, the function would return [11, 4] because the rabbit needs to eat 6 more carrots to be full, but only will eat the minimum which is 1 carrot as there are only 10 carrots remaining.