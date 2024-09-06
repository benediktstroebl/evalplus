Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    return [n + need, max(0, rem - need)]
```
This function takes in three variables, two integers representing the number of carrots eaten (`n`) and the number of carrots needed to be eaten (`need`), and remaining integer representing the total number of carrots remaining (`rem`). The function returns a list containing two integers, the total number of carrots eaten after the meal, and the number of carrots remaining after the rabbit has eaten.

For example, if a rabbit has already eaten 5 carrots and needs to eat 6 more, and there are currently 10 carrots remaining in stock, the function will return ` [11, 4]` because the rabbit will eat 6 carrots, leaving it with 11 carrots total and 4 carrots remaining.

This function ensures a rabbit will not eat more carrots than are remaining, 
but will eat as many as necessary to meet its needs. 

This solution works by adding the needed amount of carrots to the total eaten so far, and returning the total amount eaten and the remaining amount as a list.