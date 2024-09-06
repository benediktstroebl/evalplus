Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ans = [n + need, max(0, rem - need)]
    return ans
```
This function uses basic arithmetic to solve the problem by adding the `need` carrots to the total number of eaten carrots, and then subtracting that number from the remaining carrots. The result is a list with two entries, the first being the total number of carrots eaten after meals and the second being the number of carrots remaining after meals. This function adheres to the constraint of input values being less than or equal to 1000.

The code above is a simple solution to the problem, but it is important to note that it only works given the constraints provided in the prompt. Changes to these constraints may require a different solution. 

If you would like to test this function, I can provide a sample execution to validate its functionality:
```python
eat(5, 6, 10)
# Expected Output: [11, 4]
``` 
Let me know if you would like me to explain any part of the code above!  I hope this helps provide a solution to your problem.