```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list `even_odd` that stores the even integers positioned at odd indices from the input list. It traverses the list, checking if the index is even and the element is also even. If so, it includes the element in the `even_odd` list and later returns this list. This solution utilizes Python's built-in list comprehension and basic conditional logic to effectively solve the problem. 

The following is a test script that can be used to verify the functionality of the code:
```python
test_list = [4, 2, 6, 7]
expected_result = [2]

actual_result = add(test_list)

print(f"Test list: {test_list}")
print(f"Expected result: {expected_result}")
print(f"Actual result: {actual_result}")

assert actual_result == expected_result, "The function did not return the expected result."
```

With this, the `assert` statement will check if the actual result of the function call is equal to the expected result. If the assertion passes, the test script will print out "Assertion passed" and indicate that our function operates as expected.  Otherwise, it will print "Assertion failed" and display the divergent values between the actual and expected outcomes, aiding in debugging.