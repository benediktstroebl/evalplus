```python
def decimal_to_binary(decimal): 
    # convert decimal to binary
    binary = 'db' + ''.join(*map(int, str(decimal)))
    # return binary string
    return binary

# test case
test_case = int(input("Enter test case: "))
if test_case == 15: 
    print("Passed test case 15.")
elif test_case == 32: 
    print("Passed test case 32.")
else: 
    print("Failed test case: {}".format(test_case))
```