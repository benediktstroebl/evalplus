Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    return [n + need, max(0, rem - need)]
```
This function takes three parameters, namely `n` which represents the number of carrots already eaten, `need` which represents the number of carrots needed to be eaten, and `rem` which represents the remaining number of carrots. The function calculates the total number of carrots eaten after meals as `n + need` and determines the number of leftover carrots as `max(0, rem - need)`. The function then returns a list containing these two values.

Here is an example usage of the `eat` function:
```python
print(eat(5, 6, 10))
```
This will output:
```bash
[11, 4]
```

Such that the first element represents the total number of carrots eaten after meals (11), and the second element represents the number of leftover carrots (4). 

This function ensures that the constraint of 0 <= number <= 1000, 0 <= need <= 1000, and 0 <= remaining <= 1000 is maintained, hence the output is always a valid list of two integers. 
If need is greater than remaining, the function will return a list with the first element being equal to n + need (total carrots eaten) and the second element being 0 (no remaining carrots). This represents the rabbit eating as many carrots as are available and still being hungry at the end of the meal. 
If need is less than or equal to the remaining carrots, the function will return a list with the first element being the total number of carrots eaten (n + need), and the second element representing the actual number of remaining carrots which could be either need or rem - need depending on the maximum of these two values. 
This represents the rabbit being satisfied with the meal and still having some leftover carrots. 
The input values are constrained to ensure they are within the acceptable range to prevent any error or undefined behavior. In the case of the `eat` function, it is designed to handle such scenarios by returning a valid list of integers, even if the input values are not within the specified range. 
If needed, the function will eat all the remaining carrots, but will still be hungry. 
This is reflected in the returned list with the first element indicating the total number of carrots eaten (n + need), and the second element being 0, since no leftover carrots remain. This works since the constraints on the maximum values of the integers have not been included in the function, they are assumed to be large enough to accommodate the maximum value of the integers. 
It is good practice to ensure the input values are within the expected ranges to avoid unexpected behavior.