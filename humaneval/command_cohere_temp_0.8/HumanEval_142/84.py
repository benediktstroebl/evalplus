```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```
The function sums over the list, for each entry applying the respective operation based on the index criteria. The result is then returned, ensuring the list is unaffected as per the specifications. 

Here's an example of how you can use the function by calling it with a sample input list, namely `[-1,-5,2,-1,-5]`. This would output `{-126}`, which aligns with the example provided in the problem description. 

You may verify the functionality of the function with other examples provided in the problem statement. Feel free to adapt this code framework to your needs, and let me know if you require further assistance!