Here's a Python script that contains a function eat() that solves the given problem:
```python
def eat(n, need, rem):
    return [n + min(need, rem), max(0, rem - need)]
```
This function uses python's built in `min` and `max` functions to calculate the remaining number of carrots correctly. It takes into consideration the fact that if the remaining supply of carrots is less than the required amount, the rabbit will eat all remaining carrots, but still be hungry as there wouldn't be enough to fulfil the need. 

This solution corresponds to the test cases provided in the prompt, namely:
```
* eat(5, 6, 10) -> [11, 4]
* eat(4, 8, 9) -> [12, 1]
* eat(1, 10, 10) -> [11, 0]
* eat(2, 11, 5) -> [7, 0]
```
The code is self-contained and does not rely on any external variables or functions.  It can be called with the provided input to produce the expected results. 
It is concise and uses built-in Python functionalities, making it both efficient and easy to understand. 
If needed, it can be easily adapted for more complex scenarios or optimized further.