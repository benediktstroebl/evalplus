```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num = num**2
        if i % 4 == 0 and i % 3 != 0:
            num = num**3
        result += num
    return result
```
The function sums over the list and for each entry applies a corresponding transformation. The result is the sum of the transformed (or not) entries of the list. 

The logic is encapsulated in a single loop that accesses the list entries by their index 'i'. The output is the sum of the modified (or not) entries of the list. 
The function passes the test cases presented in the prompt, namely:
```
For lst = [1,2,3] the output should be 6
For lst = []  the output should be 0
For lst = [-1,-5,2,-1,-5]  the output should be -126
```
The expected outcome for the above input lists is respectively 6, 0 and -126. The function can handle any list of integers and will return the expected result. 
No further changes were made to the function as it fulfills the declaration and passes the tests presented in the prompt. 
If you wish to optimize or refactor the code to be more readable, or wish to undertake a different direction for the function, let me know and I will be happy to provide suggestions or new code. 
Other than that, hope this fulfills your request.